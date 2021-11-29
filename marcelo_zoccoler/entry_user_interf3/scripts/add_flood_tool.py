import napari

# This imports the previously generated UI file
from flood_tool import Ui_MainWindow
from skimage.io import imread
from PyQt5.QtWidgets import QMainWindow

def flood(image, delta):
    new_level = delta*85
    label_image = image <= new_level
    label_image = label_image.astype(int)*13 # label 13 is blue in napari
    return(label_image, new_level)

# Define the main window class
class MainWindow(QMainWindow,  Ui_MainWindow):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        #Initialize GUI
        self.setupUi(self)
        
        self.label_layer = None
        self.pushButton.clicked.connect(self._apply_delta)
        
    def closeEvent(self, event):
        self.close()
    
    def _apply_delta(self):
        image = self.viewer.layers['napari_island'].data
        delta = self.doubleSpinBox.value()
        label, level = flood(image, delta)
        if self.label_layer is None:
            self.label_layer = self.viewer.add_labels(label,opacity = 1)
        else:
            self.label_layer.data = label
        self.horizontalSlider.setValue(level)

napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')
viewer = napari.Viewer()
viewer.add_image(napari_image, name='napari_island')  

flood_widget = MainWindow(viewer)

dw_instance = viewer.window.add_dock_widget(flood_widget, area='right')
# napari.run()  # start the event loop and show viewer
