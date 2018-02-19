
from PyQt5 import QtCore, QtGui, QtOpenGL,QtWidgets


class SliderWithValue(QtWidgets.QSlider):

    def __init__(self, parent=None):
        super(SliderWithValue, self).__init__(parent)

        self.stylesheet = """
        QSlider::groove:vertical {
                background-color: #222;
                width: 30px;
        }

        QSlider::handle:vertical {
            border: 1px #438f99;
            border-style: outset;
            margin: -2px 0;
            width: 30px;
            height: 3px;

            background-color: #438f99;
        }

        QSlider::sub-page:vertical {
            background: #4B4B4B;
        }

        QSlider::groove:horizontal {
                background-color: #222;
                height: 30px;
        }

        QSlider::handle:horizontal {
            border: 1px #438f99;
            border-style: outset;
            margin: -2px 0;
            width: 3px;
            height: 30px;

            background-color: #438f99;
        }

        QSlider::sub-page:horizontal {
            background: #4B4B4B;
        }
        """

        self.setStyleSheet(self.stylesheet)

    def paintEvent(self, event):
        QtWidgets.QSlider.paintEvent(self, event)

        # curr_value = str(self.value() / 1000.00)
        curr_value = str(self.value())
        print 'self.value=',self.value()
        round_value = round(float(curr_value))
        print 'round_value=',round_value

        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.white))

        font_metrics = QtGui.QFontMetrics(self.font())
        font_width = font_metrics.boundingRect(str(round_value)).width()
        font_height = font_metrics.boundingRect(str(round_value)).height()

        rect = self.geometry()
        if self.orientation() == QtCore.Qt.Horizontal:
            horizontal_x_pos = rect.width() - font_width - 5
            horizontal_y_pos = rect.height() * 0.75

            painter.drawText(QtCore.QPoint(horizontal_x_pos, horizontal_y_pos), str(round_value))

        elif self.orientation() == QtCore.Qt.Vertical:
            vertical_x_pos = rect.width() - font_width - 5
            vertical_y_pos = rect.height() * 0.75

            painter.drawText(QtCore.QPoint(rect.width() / 2.0 - font_width / 2.0, rect.height() - 5), str(round_value))
        else:
            pass

        painter.drawRect(rect)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = QtWidgets.QWidget()
    win.setWindowTitle('Test Slider with Text')
    win.setMinimumSize(600, 400)
    layout = QtWidgets.QVBoxLayout()
    win.setLayout(layout)

    sliderWithValue = SliderWithValue(QtCore.Qt.Horizontal)
    sliderWithValue.setMinimum(0.0)
    sliderWithValue.setMaximum(10 * 1000)
    sliderWithValue.setTickInterval(1000)
    sliderWithValue.setSingleStep(500)
    sliderWithValue.setPageStep(1000)
    sliderWithValue.setTickPosition(QtWidgets.QSlider.TicksBelow)
    sliderWithValue.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
    sliderWithValue.setValue(1 * 1000)

    layout.addWidget(sliderWithValue)

    win.show()
    app.exec_()