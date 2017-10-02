#Steps per epoch train set.
train_num = 8000/32
#Steps per epoch test set.
test_num  = 2000/32
#Number of ephocs
epoch_numr = 100    


print ("PLEASE WAIT LOADING")

from PyQt4 import QtCore, QtGui
import cnn_trainer

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

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 200, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 100, 200, 50))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(242, 387, 291, 71))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Set Training Directory", None))
        self.pushButton.clicked.connect(self.getDirTrain)
        self.pushButton_2.setText(_translate("MainWindow", "Set Test Directory", None))
        self.pushButton_2.clicked.connect(self.getDirTest)
        self.label.setText(_translate("MainWindow", "Set Directory ", None))
        self.pushButton_3.setText(_translate("MainWindow", "Train", None))
        self.pushButton_3.clicked.connect(self.TRAIN)
    def getDirTrain(self):
        self.filTrain = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
    def getDirTest(self):
        self.filTest = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
    def TRAIN(self):
        classifier_name=input("Enter name for classifier model: ")
        mapping_name =input("Enter a name for mapping file to be generated: ")
        
        self.classifier,self.mapping=cnn_trainer.classifier_setup(self.filTrain,self.filTest , train_num , test_num, epoch_num=epoch_numr )

        self.classifier.save(classifier_name+".h5")
        

        k = open(mapping_name+".pkl","wb")
        pickle.dump(obj=mapping,file=k)
        k.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

