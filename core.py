import os
import sys
import types
import inspect
import logging

from vendor import six
from vendor.Qt import QtWidgets


logger = logging.getLogger(__name__)

_registered_plugins = {}


def install():
    discover(QtWidgets.QWidget)


def plugin_from_module(superclass, module):
    """Return plug-ins from module
    Arguments:
        superclass (superclass): Superclass of subclasses to look for
        module (types.ModuleType): Imported module from which to
            parse valid Avalon plug-ins.
    Returns:
        List of plug-ins, or empty list if none is found.
    """

    types = list()

    def recursive_bases(klass):
        r = []
        bases = klass.__bases__
        r.extend(bases)
        for base in bases:
            r.extend(recursive_bases(base))
        return r

    for name in dir(module):

        # It could be anything at this point
        obj = getattr(module, name)

        if not inspect.isclass(obj):
            continue

        # These are subclassed from nothing, not even `object`
        if not len(obj.__bases__) > 0:
            continue

        # Use string comparison rather than `issubclass`
        # in order to support reloading of this module.
        bases = recursive_bases(obj)
        if not any(base.__name__ == superclass.__name__ for base in bases):
            continue

        types.append(obj)

    return types


def discover(superclass):

    registered = _registered_plugins.get(superclass, [])
    plugins = {}

    # Current module path
    plugin_path = os.path.join(os.path.dirname(__file__), "plugins")
    # Check if plugins are useful
    for plugin in os.listdir(plugin_path):
        # Ignore files which start with underscore
        if plugin.startswith("_"):
            continue

        mod_name, mod_ext = os.path.splitext(plugin)
        if not mod_ext == ".py":
            continue

        abspath = os.path.join(plugin_path, plugin)
        if not os.path.isfile(abspath):
            continue

        module = types.ModuleType(mod_name)
        module.__file__ = abspath

        try:
            with open(abspath) as f:
                six.exec_(f.read(), module.__dict__)

            # Store reference to original module, to avoid
            # garbage collection from collecting it's global
            # imports, such as `import os`.
            sys.modules[mod_name] = module

        except Exception as err:
            logger.warning("Skipped: \"%s\" (%s)", mod_name, err)
            continue

        for plugin in plugin_from_module(superclass, module):
            if plugin.__name__ in plugins:
                print("Duplicate plug-in found: %s", plugin)
                continue

            plugins[plugin.__name__] = plugin

    for plugin in registered:
        if plugin.__name__ in plugins:
            print("Warning: Overwriting %s" % plugin.__name__)
        plugins[plugin.__name__] = plugin

    _registered_plugins.update(plugins)

    return sorted(plugins.values(), key=lambda Plugin: Plugin.__name__)


def registered_plugins():
    return _registered_plugins.copy()
