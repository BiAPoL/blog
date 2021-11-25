# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 19:54:55 2021

@author: mazo260d
"""

import napari

import sys

# This imports the previously generated UI file
from flood_tool import Ui_MainWindow
from skimage.io import imread
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget

# Define the the main window class
class MainWindow(QMainWindow,  Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        #Initialize GUI
        self.setupUi(self)
        
    def closeEvent(self, event):
        self.close()

flood_widget = MainWindow()

napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')
viewer = napari.Viewer()
viewer.add_image(napari_image, name='napari_island')   
dw_instance = viewer.window.add_dock_widget(flood_widget, area='right')
# napari.run()  # start the event loop and show viewer
        
        
        
        
        # app.quit()



# # Start the application
# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()