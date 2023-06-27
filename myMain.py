# -*- coding: utf-8 -*-
import sys
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow

from mySerial import SerialPort
from Ui_uartui_qt import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.openUARTPortButton.clicked.connect(self.openUARTPortButtonClick)

    def openUARTPortButtonClick(self):
        print('按钮被点击了！')


def comportsUARTPort():
    available_ports = serial_port.enumerate_ports()
    try:
        for port in available_ports:
            myWin.textBrowser.append(port.name + ' ' + port.description + '\r\n')
    except Exception:
        print('发生异常')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    serial_port = SerialPort()

    # 创建定时器对象，指定定时器触发后要执行的函数和时间间隔（以秒为单位）
    timer = threading.Timer(0.1, comportsUARTPort)

    # 启动定时器
    timer.start()

    available_ports = serial_port.enumerate_ports()
    print("Available ports:", available_ports)

    # for port in ports:
    #     portstr = port.name + "\t"
    #     portstr += port.description + "\t"
    #     portstr += port.device + "\n"
    #     text_box.insert(tk.END, portstr)

    sys.exit(app.exec_())
