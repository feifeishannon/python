在 PyQt 中创建窗体后，可以通过信号（signal）和槽（slot）的机制来调用按钮的功能。下面是一个简单的示例代码，演示了如何创建一个窗体，并调用按钮的点击事件：

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# 创建窗体类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)  # 设置窗体位置和大小

        button = QPushButton('点击按钮', self)  # 创建按钮
        button.setGeometry(100, 50, 100, 30)  # 设置按钮位置和大小
        button.clicked.connect(self.onButtonClick)  # 将按钮的点击信号连接到槽函数

    def onButtonClick(self):
        print('按钮被点击了！')

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建窗体对象
window = MyWindow()

# 显示窗体
window.show()

# 运行应用程序
sys.exit(app.exec_())

```

读取csv数据

```python
import sys
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
```



