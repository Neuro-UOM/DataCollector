# convert UI to Py command : pyuic5 -x TrainingMenu.ui -o TrainingMenuUI.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from TrainingMenuUI import Ui_Dialog
from AverageBandPowers import DataCollector
import threading
import time
import threading

class TrainingMenu(Ui_Dialog):

	remainingSeconds = 30 # Training Time in seconds
	REMAIN = 30

	def __init__(self, dialog):

		global chooseDirectoryText,progressBar,timeRemainingLabel,labelText

		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		chooseDirectoryText = self.chooseDirectoryText
		timeRemainingLabel = self.timeRemainingLabel
		progressBar = self.progressBar
		self.startBtn.clicked.connect(self.startBtnClicked)
		self.endBtn.clicked.connect(self.endBtnClicked)
		self.chooseDirectoryBtn.clicked.connect(self.chooseDirectoryBtnClicked)
		self.dataCollector = DataCollector()
		labelText = self.labelText

		
	def startBtnClicked(self):
		print("Start Button Clicked")
		self.dataCollector.setName(self.chooseDirectoryText.text())
		self.dataCollector.setLabel(self.labelText.text())
		self.dataCollector.start()
		self.remainingSeconds = self.REMAIN
		self.trainingTimer()
		self.changeTimer("0:30",self.REMAIN)
		self.startBtn.setEnabled(False)

	def endBtnClicked(self):
		print("End Button Clicked")
		self.remainingSeconds = 0
		progressBar.setProperty("value", 0)
		self.dataCollector.stop()
		self.startBtn.setEnabled(True)

	def chooseDirectoryBtnClicked(self):
		print("Choose Directory Button Clicked")
		
	def changeTimer(self,value,seconds):
		timeRemainingLabel.setText(value)
		# progressBar.setProperty("value", seconds)

	def trainingTimer(self):
		if(self.remainingSeconds > 0):
			threading.Timer(1.0, self.trainingTimer).start()
			self.remainingSeconds -= 1
			print("time " + str(self.remainingSeconds))
			timeString = ""
			timeString +=  str( self.remainingSeconds / 60 ) + ":"
			if (self.remainingSeconds % 60<10):
				timeString += "0"
			timeString += str( self.remainingSeconds % 60 )
			self.changeTimer(timeString,self.remainingSeconds)
			# progressBar.setProperty("value", 300 - self.remainingSeconds)
		else:
			self.dataCollector.stop()
			self.startBtn.setEnabled(True)
		


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = TrainingMenu(dialog)

	dialog.show()
	sys.exit(app.exec_()) 