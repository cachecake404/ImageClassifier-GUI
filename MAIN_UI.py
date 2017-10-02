from PyQt4 import QtCore, QtGui
import os
import subprocess

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(798, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 237, 161, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 237, 161, 81))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AI Model Trainer", None))
        self.pushButton.setText(_translate("MainWindow", "Create Model", None))
        self.pushButton_2.setText(_translate("MainWindow", "Use Model", None))

        self.pushButton.clicked.connect(self.executeC)
        self.pushButton_2.clicked.connect(self.executeU)

        self.actionOpen.setText(_translate("MainWindow", "Open", None))
    def executeC(self):
        os.system("python creation.py")
    def executeU(self):
        os.system("python usage.py")
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


#inherit this to ur class -> QtGui.QMainWindow
##        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
    
##    def getDirTrain(self):
##        self.filTrain = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
##        print self.filTrain
##    def getDirTest(self):
##        self.filTest = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
##        print self.filTest
