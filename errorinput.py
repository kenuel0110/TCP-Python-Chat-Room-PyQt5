# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorinput.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os


class Ui_DialogErrorInput(object):
    def setupUi(self, DialogErrorInput):
        DialogErrorInput.setObjectName("DialogErrorInput")
        DialogErrorInput.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        DialogErrorInput.setWindowIcon(QtGui.QIcon("icon/ico_error.ico"))
        DialogErrorInput.setFixedSize(DialogErrorInput.sizeHint())
        DialogErrorInput.setStyleSheet("background-color: rgb(56, 37, 0); color: White;")
        self.gridLayout = QtWidgets.QGridLayout(DialogErrorInput)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonok = QtWidgets.QPushButton(DialogErrorInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonok.sizePolicy().hasHeightForWidth())
        self.pushButtonok.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonok.setFont(font)
        self.pushButtonok.setStyleSheet("QPushButton {background-color: rgb(107, 71, 0);color:White;border-style: outset;border-width: 2px;border-radius: 15px;border-color: rgb(107, 71, 0);padding: 4px;}\n"
"QPushButton:pressed {background-color: #382500;color: White;border-style: outset;border-width: 2px;border-radius: 15px;border-color: #241800;padding: 4px;}")
        self.pushButtonok.setObjectName("pushButtonok")
        self.gridLayout.addWidget(self.pushButtonok, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(DialogErrorInput)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")



        self.labelIco = QtWidgets.QLabel(self.frame)

        logoPath = os.path.abspath('icon/ico_error.png')
        pixmap = QPixmap(logoPath)
        self.labelIco.setPixmap(pixmap)

        self.labelIco.setAlignment(QtCore.Qt.AlignCenter)


        self.labelIco.setObjectName("labelIco")
        self.horizontalLayout.addWidget(self.labelIco)
        self.labeltext = QtWidgets.QLabel(self.frame)
        self.labeltext.setObjectName("labeltext")
        self.horizontalLayout.addWidget(self.labeltext)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)

        self.retranslateUi(DialogErrorInput)
        self.pushButtonok.clicked.connect(DialogErrorInput.close)
        QtCore.QMetaObject.connectSlotsByName(DialogErrorInput)

    def retranslateUi(self, DialogErrorInput):
        _translate = QtCore.QCoreApplication.translate
        DialogErrorInput.setWindowTitle(_translate("DialogErrorInput", "Ошибка"))
        self.pushButtonok.setText(_translate("DialogErrorInput", "Ок"))
        self.labeltext.setText(_translate("DialogErrorInput", "<html><head/><body><p>Убедитесь, что поле ввода не пустое</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogErrorInput = QtWidgets.QDialog()
    ui = Ui_DialogErrorInput()
    ui.setupUi(DialogErrorInput)
    DialogErrorInput.show()
    sys.exit(app.exec_())