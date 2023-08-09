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

        # # 创建布局
        # layout = QVBoxLayout(self)

        # # 创建图表
        # self.figure = Figure()
        # self.canvas = FigureCanvas(self.figure)
        # layout.addWidget(self.canvas)

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
        # self.waveform_widget.plot_waveform(x, y)
        
        # self.view = self.fan1
        # self.scene = QGraphicsScene()
        # self.fan1.setScene(self.scene)
        # 在 QGraphicsScene 中绘制绿色的圆
        # green_brush = self.scene.backgroundBrush()  # 获取当前背景画刷
        # green_brush.setColor(Qt.GlobalColor.green)  # 设置画刷颜色为绿色
        # self.scene.setBackgroundBrush(green_brush)  # 将修改后的画刷应用到场景
        
        # self.view.setstyleSheet("background-color: green;")

        # circle_item = QGraphicsEllipseItem(50, 50, 100, 100)  # 创建圆形项
        # circle_item.setBrush(green_brush)  # 设置圆形项的画刷
        # self.scene.addItem(circle_item)  # 将圆形项添加到场景
        
        
        # 创建并添加 QGraphicsPixmapItem 到 QGraphicsScene，设置透明度
        # pixmap = QPixmap('your_image_path.png')
        # pixmap_item = QGraphicsPixmapItem(pixmap)
        # pixmap_item.setOpacity(0.5)  # 设置透明度
        # self.scene.addItem(pixmap_item)
        
        # 获取控件的大小
        # view_size = self.fan1.size()
        # 创建并添加 QGraphicsRectItem 到 QGraphicsScene，大小与控件相同
        # rect_item = QGraphicsRectItem(QRectF(0, 0, view_size.width(), view_size.height()))
        # rect_item.setBrush(Qt.green)
        # self.scene.addItem(rect_item)

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


class TreeNode1:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        ret = "|   " * level + "|--" + repr(self.name) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def __repr__(self):
        result = []
        
        if self.left:
            result.extend(self.left.__repr__())
        result.append(self.value)
        if self.right:
            result.extend(self.right.__repr__())
        
        return result


# # 创建二叉树
# numbers = [5, 3, 8, 1, 4, 7, 9]
# root = TreeNode(numbers[0])

# for num in numbers[1:]:
#     root.insert(num)

# # 打印二叉树的中序遍历结果，即有序数列
# sorted_sequence = root.__repr__()
# print(sorted_sequence)

# # 创建树结构
# community = TreeNode("Community")

# building1 = TreeNode("Building 1")
# building1.add_child(TreeNode("Unit A"))
# building1.add_child(TreeNode("Unit B"))

# unitA = building1.children[0]
# unitA.add_child(TreeNode("Level 1"))
# unitA.add_child(TreeNode("Level 2"))

# building2 = TreeNode("Building 2")
# building2.add_child(TreeNode("Unit C"))

# unitC = building2.children[0]
# unitC.add_child(TreeNode("Level 1"))

# community.add_child(building1)
# community.add_child(building2)

# # 打印树结构
# print(community)


# 创建应用程序对象
app = QApplication(sys.argv)

# 创建主窗口
window = MainWindow()

# 显示窗口
window.show()

# 运行应用程序
sys.exit(app.exec_())