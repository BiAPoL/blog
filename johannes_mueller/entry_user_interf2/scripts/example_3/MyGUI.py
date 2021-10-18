# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:56:18 2021

@author: johan
"""

import sys, os

# This imports the previously generated UI file
from MainWindow import Ui_MainWindow

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

# Define the the main window class
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        #Initialize GUI
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.print2label_1)
        self.horizontalSlider.valueChanged.connect(self.print2label_2)
        
    def print2label_1(self):
  
        # read value from spinbox
        value = self.spinBox.value()
        
        # print value to textlabel
        self.label.setText(f'{value}')
        
    def print2label_2(self):
  
        # read value from slider
        value = self.horizontalSlider.value()
        
        # print value to textlabel
        self.label_2.setText(f'{value}')
        
    def closeEvent(self, event):
        self.close()
        app.quit()

# Start the application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

stylefile = os.path.join(os.getcwd(), 'stylefile.qss')
window.setStyleSheet(open(stylefile, "r").read())

app.exec_()
