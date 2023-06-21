import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class WaveformWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ��������
        layout = QVBoxLayout(self)

        # ����ͼ��
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_waveform(self, x, y):
        # ���ͼ��
        self.figure.clear()

        # ����һ����ͼ
        ax = self.figure.add_subplot(111)

        # ���Ʋ���
        ax.plot(x, y)

        # ����ͼ��
        self.canvas.draw()