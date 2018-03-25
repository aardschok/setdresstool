import random

import gui.widgets as widgets
from vendor.Qt import QtWidgets
import lib


class Translate(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setFixedWidth(250)

        layout = QtWidgets.QVBoxLayout()

        seed = widgets.SliderGroup(text="Seed")
        seed.setMaxValue(2000)
        translate_y = widgets.SliderGroup(text="Translate X")
        translate_x = widgets.SliderGroup(text="Translate Y")
        translate_z = widgets.SliderGroup(text="Translate Z")

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
        layout.addWidget(translate_x)
        layout.addWidget(translate_y)
        layout.addWidget(translate_z)
        layout.addWidget(apply_btn)

        self.seed = seed
        self.relative = relative_btn
        self.absolute = absolute_btn
        self.random = random_btn
        self.apply = apply_btn

        self.translate_y = translate_y
        self.translate_x = translate_x
        self.translate_z = translate_z

        self.setLayout(layout)

        self.connections()

        self.lock_sliders()

    def connections(self):
        self.random.toggled.connect(self.lock_sliders)
        self.apply.clicked.connect(self.on_apply)

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
    w = Translate()
    w.show()

    sys.exit(app.exec_())
