# -*- coding: utf-8 -*-
import csv
import sys

from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口属性
        self.setWindowTitle("Waveform Viewer")

        # 创建波形图部件
        self.waveform_widget = WaveformWidget()

        # 设置主窗口布局
        layout = QVBoxLayout()
        layout.addWidget(self.waveform_widget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 读取 CSV 数据
        x, y = self.read_csv_data('data.csv')

        # 绘制波形图
        self.waveform_widget.plot_waveform(x, y)

    def read_csv_data(self, filename):
        x = []
        y = []

        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
        except Exception as e:
            print(f"Error reading CSV file: {e}")

        return x, y


# 创建应用程序对象
app = QApplication(sys.argv)

# 创建主窗口
window = MainWindow()

# 显示窗口
window.show()

# 运行应用程序
sys.exit(app.exec_())