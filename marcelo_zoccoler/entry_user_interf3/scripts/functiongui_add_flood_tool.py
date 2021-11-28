import napari

# This imports the previously generated UI file
from skimage.io import imread

from magicgui.widgets import FunctionGui
from napari.types import ImageData, LabelsData, LayerDataTuple

def flood(image: ImageData, delta: float=0, level: int=0) -> LayerDataTuple: 
    new_level = delta*85
    
    label_image = image <= new_level
    
    label_image = label_image.astype(int)*13 # label 13 is blue in napari

    return((label_image, {'name': 'flood result','metadata': {'new_level':new_level}}))

class MyGui(FunctionGui):
    def __init__(self):
        super().__init__(
          flood,
          call_button=True,
          layout='vertical',
          param_options={'delta':
                             {'label': 'Temperature Increase (Δ°C):', 
                              'min': 0, 'max' : 3, 'step': 0.1},
                        'level':
                            {'label':'Water Level:', 'widget_type':'Slider',
                             'min': 0, 'max' : 255}}
        )
        
    def __call__(self):
        label_image = super().__call__()
        new_level = round(label_image[1]['metadata']['new_level'])
        self.level.value = new_level


napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')
viewer = napari.Viewer()
viewer.add_image(napari_image, name='napari_island')#, colormap='viridis')   

# flood_widget = MyGui()

# dw_instance = viewer.window.add_dock_widget(flood_widget, area='right')
napari.run()  # start the event loop and show viewer




from napari_plugin_engine import napari_hook_implementation

# @napari_hook_implementation(specname="napari_experimental_provide_dock_widget")
# def main_dock_widget():
#     # you can return either a single widget, or a sequence of widgets
#     return MyGui


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return MyGui