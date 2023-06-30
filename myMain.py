# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow

from mySerial import SerThread
from Ui_uartui_qt import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.openUARTPortButton.clicked.connect(self.openUARTPortButtonClick)

    def openUARTPortButtonClick(self):
        print('按钮点击了！')


# def comportsUARTPort():
#     try:
#         available_ports = serial_port.enumerate_ports()
#         # for port in available_ports:
#             # myWin.textBrowser.append(port.device + ' ' + port.description + '\r\n')
#     except BaseException as e:
#         print(f"Failed to open serial port {serial_port.port}. Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    # 创建串口线程
    serialThread = SerThread(comb=myWin.comboBox)

    # 清空串口接收
    myWin.textBrowser.clear()
    # myWin.textBrowser.append(resultNum)
    # myWin.textBrowser.append(resultStr)
    
    serialThread.run()
    # myWin.comboBox.addItems(serialports.available_ports_descript)
    # for str in serialports:
    #     portstr = "name:" + str.name + "\t"
    #     portstr += "description:" + str.description + "\t"
    #     portstr += "device:" + str.device + "\n"
    #     myWin.textBrowser.append(portstr)
    
    # 退出应用程序的函数
    def quit_app():
        # 停止线程
        serialThread.terminate()
        # 退出应用程序
        QCoreApplication.quit()
    
    # 设置退出应用程序的信号槽
    app.aboutToQuit.connect(quit_app)
    
    sys.exit(app.exec_())
