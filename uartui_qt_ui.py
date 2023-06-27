# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uartui_qt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 40, 751, 181))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 170, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 255, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.textBrowser.setPalette(palette1)
        font = QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.openUARTPortButton = QPushButton(self.centralwidget)
        self.openUARTPortButton.setObjectName(u"openUARTPortButton")
        self.openUARTPortButton.setGeometry(QRect(170, 10, 75, 23))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 220, 751, 20))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(170, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit.setPalette(palette2)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 152, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        palette3 = QPalette()
        brush7 = QBrush(QColor(255, 170, 127, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush7)
        brush8 = QBrush(QColor(255, 170, 127, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label.setPalette(palette3)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.readAllDataButton = QPushButton(self.centralwidget)
        self.readAllDataButton.setObjectName(u"readAllDataButton")
        self.readAllDataButton.setGeometry(QRect(10, 240, 121, 26))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">test</span></p></body></html>", None))
        self.openUARTPortButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\uff1a", None))
        self.readAllDataButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6240\u6709\u6570\u636e", None))
    # retranslateUi

