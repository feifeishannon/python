# -*- coding: utf-8 -*-
import sys

import time

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen

from mySerial import SerThread
from Ui_uartui_qt import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.openUARTPortButton.clicked.connect(self.openUARTPortButtonClick)
        self.comboBox.currentIndexChanged.connect(self.comboBox_selection_change)
        self.lineEdit.returnPressed.connect(self.sendToSerial)
        self.selected = None
        # 创建串口线程
        self.serialThread = SerThread(comb=self.comboBox, textBrowser=self.textBrowser, lineEdit=self.lineEdit)

        self.serialThread.run()
        self.painter = QPainter(self.widgetdraw)
        self.painter.setRenderHint(QPainter.Antialiasing)
        
        self.widgetdraw.show()
        self.painted()
        
    def painted(self):
        # painter.begin(self.widgetdraw)
        # 设置绘制的颜色和线条样式
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor("blue"))
        self.painter.setPen(pen)

        # 绘制图形
        self.painter.drawRect(50, 50, 200, 100)  # 绘制一个矩形
        self.painter.drawEllipse(300, 100, 150, 150)  # 绘制一个椭圆
        self.painter.drawLine(500, 50, 600, 150)  # 绘制一条直线

    def openUARTPortButtonClick(self):
        if self.comboBox.count() > 0:
            self.serialThread.serialPort.serial.port = self.serialThread.serialPort.serial_dict[self.selected]
            if self.serialThread.serialPort.serial.is_open:
                self.serialThread.receive_data_flag = False
                self.serialThread.send_data_flag = False
                # self.serialThread.receive_thread.join()
                # self.serialThread.send_thread.join()
                time.sleep(0.1)
                
                self.serialThread.serialPort.serial.close()
                self.openUARTPortButton.setText("打开串口")
                print('串口被关闭！')
            else:
                self.serialThread.serialPort.serial.open()
                self.serialThread.receive_data_flag = True
                self.serialThread.send_data_flag = True
                # self.serialThread.receive_thread.start()
                # self.serialThread.send_thread.start()
                self.openUARTPortButton.setText("关闭串口")
                print('串口被打开！')

    # 关闭窗体事件
    def closeEvent(self, event):
        if self.serialThread.serialPort.serial.isOpen():
            self.serialThread.serialPort.serial.close()
        event.accept()

    def comboBox_selection_change(self, index):
        self.selected = self.comboBox.currentText()
        print("Selected port: " + self.selected)

    def sendToSerial(self):
        text = self.lineEdit.text().encode('gb2312')
        self.serialThread.data_buffer = text
        print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    # 清空串口接收
    myWin.textBrowser.clear()
    
    # 退出应用程序的函数
    def quit_app():
        # 停止线程
        myWin.serialThread.stop()
        # 退出应用程序
        QCoreApplication.quit()
    
    # 设置退出应用程序的信号槽
    app.aboutToQuit.connect(quit_app)
    
    sys.exit(app.exec_())
