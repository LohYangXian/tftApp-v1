# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadingScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time

TIME_LIMIT = 100

class Ui_LoadingWindow(object):
    def setupUi(self, LoadingWindow):
        LoadingWindow.setObjectName("LoadingWindow")
        LoadingWindow.resize(997, 587)
        LoadingWindow.setMinimumSize(QtCore.QSize(997, 587))
        LoadingWindow.setMaximumSize(QtCore.QSize(997, 587))
        LoadingWindow.setStyleSheet(" QWidget#centralwidget{border-image: url(:/newPrefix/LoadingWindow.jpg);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(LoadingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMaximum(100)
        self.progressBar.setGeometry(QtCore.QRect(220, 480, 541, 41))

            
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        LoadingWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoadingWindow)
        self.statusbar.setObjectName("statusbar")
        LoadingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoadingWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadingWindow)

    def retranslateUi(self, LoadingWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadingWindow.setWindowTitle(_translate("LoadingWindow", "MainWindow"))


class LoadingWindow(QtWidgets.QMainWindow, Ui_LoadingWindow):
    def __init__(self, parent = None):
        super(LoadingWindow,self).__init__(parent=parent)
        self.setupUi(self)


    def onClick(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(0.1)
            self.progressBar.setValue(count)


import loadingscreen_rc
import mainwindow_rc

