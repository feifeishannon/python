import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGraphicsRectItem, QGraphicsScene,
                             QGraphicsView)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    
    # 创建一个矩形图形项
    rect_item = QGraphicsRectItem(0, 0, 100, 100)
    rect_item.setBrush(Qt.blue)  # 设置矩形填充颜色
    
    
    # 将矩形添加到场景中
    scene.addItem(rect_item)
    
    view = QGraphicsView(scene)
    view.setAlignment(Qt.AlignCenter)  # 设置图形在视图中的对齐方式
    
    view.show()
    sys.exit(app.exec_())