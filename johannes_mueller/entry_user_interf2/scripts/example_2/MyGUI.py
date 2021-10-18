import sys

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
    
    def closeEvent(self, event):
        self.close()
        app.quit()
        

# Start the application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
