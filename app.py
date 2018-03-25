from vendor.Qt import QtWidgets
from gui import widgets
import core


class App(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._installed = {}

        self.setWindowTitle("SetDress Tool")

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSpacing(0)

        self.accordion_widget = widgets.AccordionWidget(self)
        self.accordion_widget.setRolloutStyle(self.accordion_widget.Maya)
        self.layout.addWidget(self.accordion_widget)

        self.setLayout(self.layout)

        self.install()

        self.setMinimumWidth(300)

    def install(self):

        core.install()
        plugins = core.registered_plugins()
        print("Found {} plugins".format(len(plugins)))
        for plugin in plugins:
            print("Installing: {}".format(plugin))

            # Retrieve the widget's class
            Plugin = plugins[plugin]
            widget = Plugin()

            self.accordion_widget.addItem(plugin.title(),
                                          self.buildFrame(widget))
            self.updateSize(widget)

    def updateSize(self, widget):
        height = (widget.sizeHint().height() - 5) + self.sizeHint().height()
        self.resize(self.sizeHint().width(), height)

        width = widget.sizeHint().width()
        self.setMinimumWidth(width + 100)

    def buildFrame(self, widget):
        """Create a frame for the widget within the accordion widget

        Args:
            widget (QtWidgets.QtWidget): the initialized widget

        Return:
            QtWidget.QFrame

        """

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(widget)
        print(widget)
        frame = QtWidgets.QFrame(self)
        frame.setLayout(vlayout)

        return frame


def show():

    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = App()
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    show()
