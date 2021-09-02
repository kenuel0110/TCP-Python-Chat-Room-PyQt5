# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messStory.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os



class Ui_MessStory(object):
    def setupUi(self, MessStory):
        MessStory.setObjectName("MessStory")
        MessStory.resize(743, 548)
        MessStory.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        MessStory.setWindowIcon(QtGui.QIcon("icon/ico_ok.ico"))
        MessStory.setStyleSheet("background-color: rgb(56, 37, 0); color: White;")
        self.gridLayout = QtWidgets.QGridLayout(MessStory)
        self.gridLayout.setContentsMargins(0, 0, 5, 5)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonok = QtWidgets.QPushButton(MessStory)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(46)
        sizePolicy.setHeightForWidth(self.pushButtonok.sizePolicy().hasHeightForWidth())
        self.pushButtonok.setSizePolicy(sizePolicy)
        self.pushButtonok.setMinimumSize(QtCore.QSize(0, 46))
        self.pushButtonok.setSizeIncrement(QtCore.QSize(0, 46))
        self.pushButtonok.setBaseSize(QtCore.QSize(0, 46))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonok.setFont(font)
        self.pushButtonok.setStyleSheet("QPushButton:!hover {background-color: rgb(61, 40, 0); text-align: center; border-style: outset; border-width: 0px;}\n"
"QPushButton:hover {background-color: rgb(88, 58, 0); text-align: center; border-style: outset; border-width: 0px;}")
        self.pushButtonok.setObjectName("pushButtonok")
        self.gridLayout.addWidget(self.pushButtonok, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(MessStory)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEditStoryMess = QtWidgets.QTextEdit(self.frame)
        self.textEditStoryMess.setStyleSheet("background-color: rgb(56, 37, 0); border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(62, 41, 0);\n"
"border-radius: 15px;\n"
"color:White;")
        self.textEditStoryMess.setObjectName("textEditStoryMess")
        self.verticalLayout.addWidget(self.textEditStoryMess)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)

        self.retranslateUi(MessStory)
        self.pushButtonok.clicked.connect(MessStory.close)
        QtCore.QMetaObject.connectSlotsByName(MessStory)
        

        checkdir = os.path.exists('users')
        if checkdir == True:
            currentNamef = open('users/current', 'r')
            currentName = str(currentNamef.readline().rstrip('\n'))
            currentNamef.close()

            encodeCurrentName = currentName.encode()
            decodeCurrentName = encodeCurrentName.decode('utf-8')
            check = os.path.exists(f'users/message/{decodeCurrentName}')
            if check == False:
                self.textEditStoryMess.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:white;\">Тут пока пусто</span></p></body></html>")
            else:

                mess = open(f'users/message/{decodeCurrentName}/messages.txt', 'r')
                self.textEditStoryMess.setText(mess.read())
                mess.close()

        self.textEditStoryMess.setReadOnly(True) 

    def retranslateUi(self, MessStory):
        _translate = QtCore.QCoreApplication.translate
        MessStory.setWindowTitle(_translate("MessStory", "История сообщений"))
        self.pushButtonok.setText(_translate("MessStory", "Закрыть"))
        self.label.setText(_translate("MessStory", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">История сообщениий</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessStory = QtWidgets.QDialog()
    ui = Ui_MessStory()
    ui.setupUi(MessStory)
    MessStory.show()
    sys.exit(app.exec_())
