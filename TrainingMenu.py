# convert UI to Py command : pyuic5 -x TrainingMenu.ui -o TrainingMenuUI.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from TrainingMenuUI import Ui_Dialog
from AverageBandPowers import DataCollector
import time
import threading


class TrainingMenu(Ui_Dialog):
	def __init__(self, dialog):
		global chooseDirectoryText,progressBar
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		chooseDirectoryText = self.chooseDirectoryText
		progressBar = self.progressBar		
		self.startBtn.clicked.connect(self.startBtnClicked)
		self.endBtn.clicked.connect(self.endBtnClicked)
		self.chooseDirectoryBtn.clicked.connect(self.chooseDirectoryBtnClicked)
		self.dataCollector = DataCollector()

		
	def startBtnClicked(self):
		print("Start Button Clicked")
		# threading.Thread(self.dataCollector.setFileName(self.chooseDirectoryText.text())).Start()
		# self.dataCollector.start(self.chooseDirectoryText.text())
		self.dataCollector.setName(self.chooseDirectoryText.text())
		self.dataCollector.start()

	def endBtnClicked(self):
		print("End Button Clicked")
		progressBar.setProperty("value", 0)
		self.dataCollector.stop()

	def chooseDirectoryBtnClicked(self):
		print("Choose Directory Button Clicked")
		
	

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = TrainingMenu(dialog)

	dialog.show()
	sys.exit(app.exec_()) 