import sys
import threading
import string

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
    try:
        available_ports = serial_port.enumerate_ports()
        # for port in available_ports:
            # myWin.textBrowser.append(port.device + ' ' + port.description + '\r\n')
    except BaseException as e:
        print(f"Failed to open serial port {serial_port.port}. Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    serial_port = SerialPort()

    # 创建定时器对象，指定定时器触发后要执行的函数和时间间隔（以秒为单位）
    timer = threading.Timer(0.1, comportsUARTPort)

    # 启动定时器
    a='bba6081'
    b='5f6661'
    combinations = [f"{n1}{n2}{c}" for n1 in range(10) for n2 in range(10) for c in string.ascii_lowercase]
    myWin.textBrowser.clear()
    # myWin.textBrowser.append(resultNum)
    # myWin.textBrowser.append(resultStr)
    for str in combinations:
        myWin.textBrowser.append(a+str+b)
    
    timer.start()
    
    # for port in ports:
    #     portstr = port.name + "\t"
    #     portstr += port.description + "\t"
    #     portstr += port.device + "\n"
    #     text_box.insert(tk.END, portstr)

    sys.exit(app.exec_())
