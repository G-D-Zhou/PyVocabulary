# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMainApp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_Paraphrase = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Paraphrase.setGeometry(QtCore.QRect(460, 150, 231, 61))
        self.textBrowser_Paraphrase.setObjectName("textBrowser_Paraphrase")
        self.textBrowser_phonetics = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_phonetics.setGeometry(QtCore.QRect(280, 150, 171, 61))
        self.textBrowser_phonetics.setObjectName("textBrowser_phonetics")
        self.textBrowser_word = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_word.setGeometry(QtCore.QRect(60, 150, 211, 61))
        self.textBrowser_word.setObjectName("textBrowser_word")
        self.lineEdit_location = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_location.setGeometry(QtCore.QRect(140, 30, 113, 21))
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 61, 16))
        self.label.setObjectName("label")
        self.pushButton_location = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_location.setGeometry(QtCore.QRect(250, 30, 31, 21))
        self.pushButton_location.setObjectName("pushButton_location")
        self.textBrowser_location = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_location.setGeometry(QtCore.QRect(300, 30, 371, 71))
        self.textBrowser_location.setObjectName("textBrowser_location")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(390, 250, 113, 32))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_Previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Previous.setGeometry(QtCore.QRect(230, 250, 113, 32))
        self.pushButton_Previous.setObjectName("pushButton_Previous")
        self.pushButton_goback = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_goback.setGeometry(QtCore.QRect(70, 250, 113, 32))
        self.pushButton_goback.setObjectName("pushButton_goback")
        self.pushButton_player = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_player.setGeometry(QtCore.QRect(550, 250, 113, 32))
        self.pushButton_player.setObjectName("pushButton_player")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "专业词汇记忆软件-V0.3"))
        self.label.setText(_translate("MainWindow", "选择词库: "))
        self.pushButton_location.setText(_translate("MainWindow", "..."))
        self.pushButton_next.setText(_translate("MainWindow", "下一个"))
        self.pushButton_Previous.setText(_translate("MainWindow", "上一个"))
        self.pushButton_goback.setText(_translate("MainWindow", "回到第一个"))
        self.pushButton_player.setText(_translate("MainWindow", "发音"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

