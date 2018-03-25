import random

from vendor.Qt import QtWidgets

from ui import widgets
import lib


class Rotate(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setFixedWidth(250)

        layout = QtWidgets.QVBoxLayout()

        seed = widgets.SliderGroup(text="Seed")
        seed.setMaxValue(2000)
        rotate_y = widgets.SliderGroup(text="Rotate X")
        rotate_x = widgets.SliderGroup(text="Rotate Y")
        rotate_z = widgets.SliderGroup(text="Rotate Z")

        options_layout = QtWidgets.QHBoxLayout()

        relative_btn = QtWidgets.QRadioButton("Relative")
        absolute_btn = QtWidgets.QRadioButton("Absolute")
        random_btn = QtWidgets.QRadioButton("Random")
        relative_btn.setChecked(True)

        apply_btn = QtWidgets.QPushButton("Apply")

        options_layout.addWidget(absolute_btn)
        options_layout.addWidget(relative_btn)
        options_layout.addWidget(random_btn)

        layout.addLayout(options_layout)
        layout.addWidget(seed)
        layout.addWidget(rotate_y)
        layout.addWidget(rotate_x)
        layout.addWidget(rotate_z)
        layout.addWidget(apply_btn)

        self.seed = seed
        self.relative = relative_btn
        self.absolute = absolute_btn
        self.random = random_btn
        self.apply = apply_btn

        self.translate_y = rotate_y
        self.translate_x = rotate_x
        self.translate_z = rotate_z

        self.setLayout(layout)

        self.connections()

        self.lock_sliders()

    def connections(self):
        self.random.toggled.connect(self.lock_sliders)

    def lock_sliders(self):

        state = not self.random.isChecked()
        self.translate_x.setEnabled(state)
        self.translate_y.setEnabled(state)
        self.translate_z.setEnabled(state)
        self.seed.setEnabled(not state)

    def on_apply(self):

        if self.random.isChecked():
            approach = random.choice(["relative", "absolute"])
            x = random.seed(self.seed.getValue())
            y = random.seed(self.seed.getValue())
            z = random.seed(self.seed.getValue())
        else:
            approach = "relative" if self.relative.isChecked() else "absolute"
            x = self.translate_x.getValue()
            y = self.translate_y.getValue()
            z = self.translate_z.getValue()

        lib.translate_offset(x, y, z, approach=approach)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Rotate()
    w.show()

    sys.exit(app.exec_())
