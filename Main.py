from riotwatcher import TftWatcher, ApiError
from ApiKey import *
from getters import *
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from MainWindow import *




app = qtw.QApplication([])
mw = Ui_MainWindow()

app.exec_()