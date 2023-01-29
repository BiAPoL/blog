import napari
from skimage.io import imread
from magicgui import magicgui
from napari.types import ImageData, LabelsData

def flood(image: ImageData, delta: float=0, new_level: int=0) -> LabelsData:
    new_level = delta*85
    label_image = image <= new_level
    label_image = label_image.astype(int)*13 # label 13 is blue in napari
    return(label_image)

viewer = napari.Viewer()
napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')    # Reads an image from file
viewer.add_image(napari_image, name='napari_island')                       # Adds the image to the viewer and give the image layer a name

flood_widget = magicgui(flood, delta={'label': 'Temperature Increase (Δ°C):',  # Create GUI with magicgui
                                           'min': 0, 'max' : 3, 'step': 0.1},
                                new_level={'label':'Sea Level (dm):', 'widget_type':'Slider',
                                           'min': 0, 'max' : 255, "enabled": False},
                                auto_call=True)

# Thalley Lambert contributed to the annotated function below
@flood_widget.delta.changed.connect  # Connect a function to delta (spinbox widget)
def update_level(delta: float):
    flood_widget.new_level.value = delta * 85  # Update slider when spinbox changes

viewer.window.add_dock_widget(flood_widget, area='right')  # Add our gui instance to napari viewer

