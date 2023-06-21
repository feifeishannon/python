�� PyQt �д�������󣬿���ͨ���źţ�signal���Ͳۣ�slot���Ļ��������ð�ť�Ĺ��ܡ�������һ���򵥵�ʾ�����룬��ʾ����δ���һ�����壬�����ð�ť�ĵ���¼���

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# ����������
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)  # ���ô���λ�úʹ�С

        button = QPushButton('�����ť', self)  # ������ť
        button.setGeometry(100, 50, 100, 30)  # ���ð�ťλ�úʹ�С
        button.clicked.connect(self.onButtonClick)  # ����ť�ĵ���ź����ӵ��ۺ���

    def onButtonClick(self):
        print('��ť������ˣ�')

# ����Ӧ�ó������
app = QApplication(sys.argv)

# �����������
window = MyWindow()

# ��ʾ����
window.show()

# ����Ӧ�ó���
sys.exit(app.exec_())

```

��ȡcsv����

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ���ô�������
        self.setWindowTitle("Waveform Viewer")

        # ��������ͼ����
        self.waveform_widget = WaveformWidget()

        # ���������ڲ���
        layout = QVBoxLayout()
        layout.addWidget(self.waveform_widget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # ��ȡ CSV ����
        x, y = self.read_csv_data('data.csv')

        # ���Ʋ���ͼ
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


# ����Ӧ�ó������
app = QApplication(sys.argv)

# ����������
window = MainWindow()

# ��ʾ����
window.show()

# ����Ӧ�ó���
sys.exit(app.exec_())
```



