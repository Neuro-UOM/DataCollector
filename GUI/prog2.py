# convert UI to Py command : pyuic5 -x secondgui.ui -o secondgui.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from secondgui import Ui_Dialog

class MyFirstGuiProgram(Ui_Dialog):
	def __init__(self, dialog):
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = MyFirstGuiProgram(dialog)

	dialog.show()
	sys.exit(app.exec_()) 