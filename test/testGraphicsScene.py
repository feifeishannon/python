import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGraphicsRectItem, QGraphicsScene,
                             QGraphicsView)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    
    # ����һ������ͼ����
    rect_item = QGraphicsRectItem(0, 0, 100, 100)
    rect_item.setBrush(Qt.blue)  # ���þ��������ɫ
    
    
    # ��������ӵ�������
    scene.addItem(rect_item)
    
    view = QGraphicsView(scene)
    view.setAlignment(Qt.AlignCenter)  # ����ͼ������ͼ�еĶ��뷽ʽ
    
    view.show()
    sys.exit(app.exec_())