"""

    This module generate a simple placeholder frame without any contents.

"""

from PyQt5.QtWidgets import QFrame

class Frame(QFrame):

    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args)

        # Lambda func grab input args
        get_param = lambda x : kwargs.get(x)

        height = get_param("height")
        width = get_param("width")
        name = get_param("name")
        stylesheet = get_param("stylesheet")

        # Set size
        height and self.setFixedHeight(height)
        width and self.setFixedWidth(width)

        # Set property if given
        name and self.setObjectName(name)
        stylesheet and self.setObjectName(name)


