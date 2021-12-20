import napari
from skimage.io import imread
from napari.types import ImageData, LabelsData, LayerDataTuple
from magicgui.widgets import FunctionGui

def flood(image: ImageData, delta: float=0, new_level: int=0) -> LayerDataTuple:
    new_level = delta*85
    label_image = image <= new_level
    label_image = label_image.astype(int)*13 # label 13 is blue in napari
    return((label_image, {'name': 'flood result','metadata': {'new_level':new_level}}))

class MyGui(FunctionGui):
    def __init__(self):
        super().__init__(
          flood,
          call_button=False,
          auto_call=True,
          layout='vertical',
          param_options={'delta':
                             {'label': 'Temperature Increase (Δ°C):',
                              'min': 0, 'max' : 3, 'step': 0.1},
                        'new_level':
                            {'label':'Sea Level (dm):', 'widget_type':'Slider',
                             'min': 0, 'max' : 255, 'enabled' : False}}
        )

    def __call__(self):
        label_image = super().__call__()
        new_level = round(label_image[1]['metadata']['new_level'])
        self.new_level.value = new_level


napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')
viewer = napari.Viewer()
viewer.add_image(napari_image, name='napari_island')

flood_widget = MyGui()
viewer.window.add_dock_widget(flood_widget, area='right')