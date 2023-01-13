import napari
from skimage.io import imread
from qtpy.QtWidgets import QMainWindow
from qtpy import uic
from pathlib import Path

def flood(image, delta):
    new_level = delta*85
    label_image = image <= new_level
    label_image = label_image.astype(int)*13  # label 13 is blue in napari
    return(label_image, new_level)

# Define the main window class
class FancyGUI(QMainWindow):
    def __init__(self, napari_viewer):          # include napari_viewer as argument (it has to have this name)
        super().__init__()
        self.viewer = napari_viewer
        self.UI_FILE = str(Path(__file__).parent / "flood_tool.ui")  # path to .ui file
        uic.loadUi(self.UI_FILE, self)           # load QtDesigner .ui file

        self.label_layer = None                # stored label layer variable
        self.pushButton.clicked.connect(self.apply_delta)

    def apply_delta(self):
        image = self.viewer.layers['napari_island'].data    # We chose to use the layer name to find the correct image layer
        delta = self.doubleSpinBox.value()
        label, level = flood(image, delta)
        if self.label_layer is None:
            self.label_layer = self.viewer.add_labels(label)
        else:
            self.label_layer.data = label
        self.horizontalSlider.setValue(level)

viewer = napari.Viewer()
napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')    # Reads an image from file
viewer.add_image(napari_image, name='napari_island')                       # Adds the image to the viewer and give the image layer a name

flood_widget = FancyGUI(viewer)                                          # Create instance from our class
viewer.window.add_dock_widget(flood_widget, area='right')                  # Add our gui instance to napari viewer
