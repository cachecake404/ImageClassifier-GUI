print("PLEASE WAIT LOADING")
from PyQt4 import QtCore, QtGui
import pickle
import numpy as np
from keras.preprocessing import image
from keras.models import load_model

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
        self.pushButton.setGeometry(QtCore.QRect(220, 100, 351, 121))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 380, 351, 121))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 240, 351, 121))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Load Model", None))
        self.pushButton.clicked.connect(self.setModel)
        self.pushButton_2.setText(_translate("MainWindow", "Test Image", None))
        self.pushButton_2.clicked.connect(self.testimg)
        self.pushButton_3.setText(_translate("MainWindow", "Load Mapping", None))
        self.pushButton_3.clicked.connect(self.setMap)
    def setMap(self):
        self.mappindir = QtGui.QFileDialog.getOpenFileName(self,'Set Mapping File')
        mapin = open(self.mappindir,'rb')
        self.mapping = pickle.load(mapin)
    def setModel(self):

        self.modeldir = QtGui.QFileDialog.getOpenFileName(self,'Set Model/Classifier File')
        self.model=load_model(self.modeldir)
        
    def testimg(self):
        self.imgdir = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        try:
            result = self.model_predict(self.model,self.mapping,self.imgdir)
            print(result)
        except Exception as e:
            print("Please make sure you load model and mapping file!")
            print("Specific error is \n")
            print(str(e)+"\n")
            
        
    def model_predict(self,model,mapping,test_dir):
        pic = image.load_img(test_dir,target_size=(150,150))
        pic = image.img_to_array(pic)
        pic = np.expand_dims(pic,axis=0)
        result = model.predict(pic)
        return self.simplify(mapping,result[0][0])

    def simplify(self,mapping,result):
        for i in mapping:
            if mapping[i] == result:
                key = i
                break
        return key


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


