import napari
# This imports the previously generated UI file
from skimage.io import imread

from magicgui import magicgui
from napari.types import ImageData, LabelsData

def flood(image: ImageData, delta: float=0, level: int=0) -> LabelsData: 
    new_level = delta*85
    
    label_image = image <= new_level
    
    label_image = label_image.astype(int)*13 # label 13 is blue in napari

    return(label_image)

napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')
viewer = napari.Viewer()
viewer.add_image(napari_image, name='napari_island')#, colormap='viridis')   

flood_widget = magicgui(flood, delta={'label': 'Temperature Increase (Δ°C):', 
                                           'min': 0, 'max' : 3, 'step': 0.1},
                                    level={'label':'Water Level:', 'widget_type':'Slider',
                                           'min': 0, 'max' : 255})

dw_instance = viewer.window.add_dock_widget(flood_widget, area='right')
napari.run()  # start the event loop and show viewer

