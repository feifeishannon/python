import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class WaveformWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建布局
        layout = QVBoxLayout(self)

        # 创建图表
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def plot_waveform(self, x, y):
        # 清空图表
        self.figure.clear()

        # 创建一个子图
        ax = self.figure.add_subplot(111)

        # 绘制波形
        ax.plot(x, y)

        # 更新图表
        self.canvas.draw()