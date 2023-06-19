import sys

from PyQt5.QtWidgets import QApplication, QDialog

from mySerial import SerialPort
from Ui_uartui_qt import Ui_Dialog


class MyDialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        print('按钮被点击了！')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyDialog()
    myWin.show()

    #
    serial_port = SerialPort()

    # 
    available_ports = serial_port.enumerate_ports()
    print("Available ports:", available_ports)

    # for port in ports:
    #     portstr = port.name + "\t"
    #     portstr += port.description + "\t"
    #     portstr += port.device + "\n"
    #     text_box.insert(tk.END, portstr)

    sys.exit(app.exec_())
