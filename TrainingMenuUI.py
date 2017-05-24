# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrainingMenu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(958, 584)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(580, 520, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 200, 891, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.endBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.endBtn.setObjectName("endBtn")
        self.horizontalLayout.addWidget(self.endBtn)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 100, 71, 31))
        self.label.setObjectName("label")
        self.chooseDirectoryText = QtWidgets.QLineEdit(Dialog)
        self.chooseDirectoryText.setGeometry(QtCore.QRect(130, 100, 721, 31))
        self.chooseDirectoryText.setObjectName("chooseDirectoryText")
        self.chooseDirectoryBtn = QtWidgets.QPushButton(Dialog)
        self.chooseDirectoryBtn.setGeometry(QtCore.QRect(860, 100, 41, 31))
        self.chooseDirectoryBtn.setObjectName("chooseDirectoryBtn")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 350, 111, 21))
        self.label_2.setObjectName("label_2")
        self.timeRemainingLabel = QtWidgets.QLabel(Dialog)
        self.timeRemainingLabel.setGeometry(QtCore.QRect(290, 390, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(36)
        self.timeRemainingLabel.setFont(font)
        self.timeRemainingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeRemainingLabel.setObjectName("timeRemainingLabel")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startBtn.setText(_translate("Dialog", "Start"))
        self.endBtn.setText(_translate("Dialog", "End"))
        self.label.setText(_translate("Dialog", "Data Log"))
        self.chooseDirectoryBtn.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "Time Remaining"))
        self.timeRemainingLabel.setText(_translate("Dialog", "5:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

