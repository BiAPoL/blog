from qtpy.QtWidgets import QWidget
from qtpy.QtCore import QEvent, QObject
from qtpy import uic
from pathlib import Path

from magicgui.widgets import create_widget
from napari.layers import Image


class my_custom_widget(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()

        self.viewer = napari_viewer
        uic.loadUi(Path(__file__).parent / "./complex_widget.ui", self)

        # add magicgui widget to widget layout
        self.image_layer_select = create_widget(annotation=Image,
                                                label="Image_layer")
        self.layout().insertWidget(0, self.image_layer_select.native)
        self.installEventFilter(self)

        # connect slider to function
        self.horizontal_slider_widget.valueChanged.connect(self.on_slider_change)

    def eventFilter(self, obj: QObject, event: QEvent):
        if event.type() == QEvent.ParentChange:
            self.image_layer_select.parent_changed.emit(self.parent())

        return super().eventFilter(obj, event)

    def on_slider_change(self):
        image_layer = self.image_layer_select.value
        binary_image = image_layer.data > self.horizontal_slider_widget.value()

        if 'result of threshold' not in self.viewer.layers:
            self.viewer.add_image(binary_image,
                                  name='result of threshold',
                                  opacity=0.5)
        else: 
            self.viewer.layers['result of threshold'].data = binary_image