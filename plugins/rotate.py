import random

from vendor.Qt import QtWidgets
import gui.widgets as widgets
import lib


class Rotate(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setFixedWidth(250)

        layout = QtWidgets.QVBoxLayout()

        random_range_hlayout = QtWidgets.QHBoxLayout()

        min_vlayout = QtWidgets.QVBoxLayout()
        min_label = QtWidgets.QLabel("Min value")
        min_range = QtWidgets.QDoubleSpinBox()
        min_range.setMinimum(-360)
        min_range.setValue(-360)
        min_vlayout.addWidget(min_label)
        min_vlayout.addWidget(min_range)

        max_vlayout = QtWidgets.QVBoxLayout()
        max_label = QtWidgets.QLabel("Max value")
        max_range = QtWidgets.QDoubleSpinBox()
        max_range.setMaximum(360)
        max_range.setValue(360)
        max_vlayout.addWidget(max_label)
        max_vlayout.addWidget(max_range)

        random_range_hlayout.addLayout(min_vlayout)
        random_range_hlayout.addLayout(max_vlayout)

        # Default sliders
        rotate_y = widgets.SliderGroup(text="Rotate X")
        rotate_y.setMinValue(-360)
        rotate_y.setMaxValue(360)

        rotate_x = widgets.SliderGroup(text="Rotate Y")
        rotate_x.setMinValue(-360)
        rotate_x.setMaxValue(360)

        rotate_z = widgets.SliderGroup(text="Rotate Z")
        rotate_z.setMinValue(-360)
        rotate_z.setMaxValue(360)

        options_layout = QtWidgets.QHBoxLayout()

        relative_btn = QtWidgets.QRadioButton("Relative")
        absolute_btn = QtWidgets.QRadioButton("Absolute")
        random_btn = QtWidgets.QCheckBox("Random")
        relative_btn.setChecked(True)

        apply_btn = QtWidgets.QPushButton("Apply")

        options_layout.addWidget(absolute_btn)
        options_layout.addWidget(relative_btn)
        options_layout.addWidget(random_btn)

        layout.addLayout(options_layout)
        layout.addLayout(random_range_hlayout)
        layout.addWidget(rotate_y)
        layout.addWidget(rotate_x)
        layout.addWidget(rotate_z)
        layout.addWidget(apply_btn)

        self.relative = relative_btn
        self.absolute = absolute_btn
        self.random = random_btn
        self.min_value = min_range
        self.max_value = max_range
        self.apply = apply_btn

        self.rotate_y = rotate_y
        self.rotate_x = rotate_x
        self.rotate_z = rotate_z

        self.setLayout(layout)

        self.connections()

        self.lock_sliders()

    def connections(self):
        self.random.toggled.connect(self.lock_sliders)
        self.apply.clicked.connect(self.on_apply)

    def lock_sliders(self):

        state = not self.random.isChecked()

        self.rotate_x.setEnabled(state)
        self.rotate_y.setEnabled(state)
        self.rotate_z.setEnabled(state)

        self.min_value.setEnabled(not state)
        self.max_value.setEnabled(not state)

    def on_apply(self):

        approach = "relative" if self.relative.isChecked() else "absolute"
        if self.random.isChecked():
            min_range = self.min_value.value()
            max_range = self.max_value.value()
            x = random.uniform(min_range, max_range)
            y = random.uniform(min_range, max_range)
            z = random.uniform(min_range, max_range)
        else:
            x = self.rotate_x.getValue()
            y = self.rotate_y.getValue()
            z = self.rotate_z.getValue()

        lib.rotate_offset(x, y, z, approach=approach)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Rotate()
    w.show()

    sys.exit(app.exec_())
