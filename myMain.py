# -*- coding: utf-8 -*-
import sys

import time

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow

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
        # 鍒涘缓涓插彛绾跨▼
        self.serialThread = SerThread(comb=self.comboBox, textBrowser=self.textBrowser, lineEdit=self.lineEdit)

        self.serialThread.run()
        
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
                self.openUARTPortButton.setText("鎵撳紑涓插彛")
                print('涓插彛琚�鍏抽棴锛�')
            else:
                self.serialThread.serialPort.serial.open()
                self.serialThread.receive_data_flag = True
                self.serialThread.send_data_flag = True
                # self.serialThread.receive_thread.start()
                # self.serialThread.send_thread.start()
                self.openUARTPortButton.setText("鍏抽棴涓插彛")
                print('涓插彛琚�鎵撳紑锛�')

    # 鍏抽棴绐椾綋浜嬩欢
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

    # 娓呯┖涓插彛鎺ユ敹
    myWin.textBrowser.clear()
    
    # 閫€鍑哄簲鐢ㄧ▼搴忕殑鍑芥暟
    def quit_app():
        # 鍋滄�㈢嚎绋�
        myWin.serialThread.stop()
        # 閫€鍑哄簲鐢ㄧ▼搴�
        QCoreApplication.quit()
    
    # 璁剧疆閫€鍑哄簲鐢ㄧ▼搴忕殑淇″彿妲�
    app.aboutToQuit.connect(quit_app)
    
    sys.exit(app.exec_())
