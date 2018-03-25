from maya import cmds


def translate_offset(x, y, z, approach):
    """Translate the current select to a position

    Args:
        x (int, float): value to move along x axis
        y (int, float): value to move along y axis
        z (int, float): value to move along z axis
        approach (str): method in which the action will take place, eg: relative

    Returns:
        None

    """
    selection = cmds.ls(selection=True, type="transform")
    cmds.move(selection, x, y, z, **{approach: True})


def rotate_offset(x, y, z, approach):
    """Rotate the current select to a position

    Args:
        x (int, float): value to move along x axis
        y (int, float): value to move along y axis
        z (int, float): value to move along z axis
        approach (str): method in which the action will take place, eg: relative

    Returns:
        None

    """
    selection = cmds.ls(selection=True, type="transform")
    cmds.rotate(selection, x, y, z, **{approach: True})
