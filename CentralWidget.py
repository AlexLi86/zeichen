from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtWidgets import QWidget, QSlider, QLabel, QTextEdit, QVBoxLayout, QPushButton, QApplication, QTextBrowser, \
    QGridLayout, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)


        self.update()

    def paintEvent(self, a0) -> None:
        super(CentralWidget, self).paintEvent(a0)

        pen = QPen()
        pen.setColor(QColor("red"))
        pen.setWidth(25)
        pen.setStyle(Qt.PenStyle.DashDotDotLine)


        brush = QBrush(QColor("cyan"))
        brush.setStyle(Qt.BrushStyle(Qt.BrushStyle.Dense7Pattern))

        painter = QPainter(self)
        painter.setPen(pen)
        painter.setBrush(brush)


        painter.drawEllipse(100, 50, 200, 300)