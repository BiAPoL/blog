# Custom user interfaces for Python (Part 2)
[Johannes Müller](../Readme), October 18th 2021

## Introduction
Graphical user interfaces (*GUIs*) are powerful tools to make your scripts and functions available to users that are not necessarily familiar with a lot of coding, development platforms (e.g. Spyder or PyCharm) - and shouldn't be experienced programmers in order to use your tools.

In this blog, we will cover a few interesting and versatile methods for you to create customized [Qt](https://qt.io)-based GUIs for Python in general. Since our work revolves mostly around the visualization and processing of **images**, we will also show you a few ways to create great user interfaces for [Napari](https://napari.org/).

Blogs on this topic will cover:
* [Getting started (Part 1)](../entry_user_inter/Readme#getting-started)
* [Creating standalone GUIs (Part 2)](#creating-advanced-standalone-guis)
* [Creating GUIs for napari (Part 3)](../../marcelo_zoccoler/entry_user_interf3/Readme#creating-advanced-guis-for-napari)
* [Turning napari GUI into plugins (Part 4)](../../marcelo_zoccoler/entry_user_interf4/Readme#turning-napari-gui-into-plugins)


# Creating advanced standalone GUIs
The [previous entry](../entry_user_inter/Readme#getting-started) showed you how to create basic GUIs by setting up a ```QMainWindow``` object and adding basic objects, such as buttons to it. However, especially if user interfaces become more complex, the approach of manually adding elements to your window will become harder and harder to control. This part of the tutorial will cover the creation of advanced user interfaces for PyQt.

## Table of contents
* [Creating your environment](#creating-your-environment)
* [The Qt Designer](#the-qt-designer)
* [Designing a simple GUI with the Designer](#creating-a-simple-gui-with-the-designer)
* [Converting the GUI to .py file and GUI creation](#convert-gui-to-py-file-and-gui-creation)
* [Adding functionality to GUI (a.k.a. signals and slots)](#adding-functionality-to-gui-aka-signals-and-slots)
* [Adding a matplotlib widget to a GUI with Qt Designer](#adding-a-matplotlib-widget-to-a-gui-with-qt-designer)
* [Bonus: Adding a cool style to your GUI](#bonus-adding-a-cool-style-to-your-gui)

## Creating your environment
It is highly recommended to create a separate conda environment. Many programs in the Python ecosystem somehow rely on PyQt, so messing around with PyQt in environments can easily break things (Been there, done that). In the Anaconda command line, navigate to your desired folder and create a new conda environment:

```
conda create -n PyQt_GUI
conda activate PyQt_GUI
```
I work mostly with jupyter notebooks or Spyder, so you can download both and pick your preferred platform
```
conda install jupyter spyder
```

## The Qt Designer
The Qt Designer is one of the hidden champions of programs that are shipped with Anaconda Navigator. If you have Anaconda installed, you can find it in Windows by simply searching for "designer". Otherwise, it is usually located at ```C:\Users\Username\anaconda3\Library\bin\designer.exe```. Starting it brings up this dialogue:

![designer_start](https://user-images.githubusercontent.com/38459088/137153642-d0372482-4f1b-453d-81ce-6a82d8b73c8c.JPG)

Create a main window by clicking "Main Window" from the list and then ```Create```. This brings up a blank window which you can now populate with widgets. Let's go through the elements!

![designer_overview](https://user-images.githubusercontent.com/38459088/137155868-38158b26-2ad3-4065-ac9d-6846de3ef349.png)

* *Widgets* (orange): This part of the designer lists all available widgets, like buttons or sliders, but also more advanced items like dropdown menus or tab windows that allow you to generate several pages in your GUI (similar to tabs in your browser). You can put widgets onto your main window simply by **drag & drop**.
* *Layouts* (blue): Once you have dropped widgets on your main window, you can either leave them as they are, or arrange them in a **layout**. This will align them nicely and allow Qt to rescale your items properly if the size of the main window is changed.
* *Widget properties* (purple): Every widget has a set of properties, all of which are displayed in the rightmost box. For instance, every placed widget has a property ```objectName```, which is the name by which you can address it later on in your code. It also allows to set **default values or allowed ranges for input** (e.g., min/max values for sliders)

## Creating a simple GUI with the Designer
In order to create a functioning GUI for Python, a few steps are necessary. First, let's create a simple GUI by adding a SpinBox, a Button and a Textlabel to the GUI (top row). The bottom row consists of a horizontal slider and another textlabel widget. Double clicking on the pushButton allows you to change the text on the button. Selecting the grid layout from the layouts box arranges these in a nice fashion:

![simple_GUI](https://user-images.githubusercontent.com/38459088/137158206-c35b8fa2-6d9e-46d0-b98a-fd56a2de75dd.JPG)

Inspecting the widgets properties tells us that the widgets have the following default ```objectName``` (You can change this to any value you like, but every widget has to have a **unique name**):
* SpinBox widget: ```spinBox```
* Button widget: ```pushButton```
* Upper textlabel widget: ```label```
* Lower textlabel widget: ```label_2```
* Horizontal slider widget: ```horizontalSlider```

## Convert GUI to .py file and GUI creation
Now, save your design file in your project directory as ```MyGUI.ui```. The generated .ui file is at this point not readable for Python. Then use an anaconda command prompt and navigate to the location of ```MyGUI.ui```. You can convert it to a Python file with the following command:
```
pyuic5 MainWindow.ui -o MainWindow.py
```
This creates a Python script at the same location (or at any location you specify after the ```-o``` flag) that looks like this:

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(242, 110)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 242, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Print"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
```

Tada 🎉 🎉 🎉 this is all the Python needs to know to create the GUI. As you can see, it would be very complicated to generate a window layout like this from code alone. As the (autogenerated) note on the top says: It makes no sense to make changes to this file, as it will be overwritten whenever you make changes to you MainWindow.ui (for instance by adding or renaming widgets) and run ```pyuic5```.

Now, let's write a little script that is able to load and use our layout. The important part is the call of ```self.setupUi(self)```, which has been automatically defined in MainWindow.py. Adding ```Ui_MainWindow``` as an argument to the definition of ```class MainWindow(...)``` allows us to use its functions (e.g., ```setupUi()```) for our own GUI:

```python
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

```

## Adding functionality to GUI (a.k.a. signals and slots)
Now that we have created the GUI, we want to interact with its elements. This tutorial will cover two examples:

1. Using a button to read the value from a SpinBox and print it to a textfield

To do this, we add a function to the ```MainWindow``` class that reads the value from the SpinBox and prints it to the TextLabel. Note that the names of the widgets in the code are simply the ```objectName``` we defined earlier in the Qt Designer.

```python
  def print2label_1(self):
  
    # read value from spinbox
    value = self.spinBox.Value()
    
    # print value to textlabel
    self.label.setText(f'{value}')
```

Next, we connect the button to the ```print2label``` in the ```__init__()``` function:
```python
    self.pushButton.clicked.connect(self.print2label)
```

2. Printing the values of a slider to a textfield whenever the slider is moved:

This is helpful if the GUI should update live while an input value is changed (e.g., a slider is moved). To do this, we need a similar function:
```python
  def print2label_2(self):
  
    # read value from spinbox
    value = self.horizontalSlider.Value()
    
    # print value to textlabel
    self.label_2.setText(f'{value}')
```
and connect this function in the ```__init__()``` statement:
```python
    self.horizontalSlider.valueChanged.connect(self.print2label_2)
```

Here is the complete code:
```python
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

app.exec_()
```
You find all code from this example [here](https://github.com/BiAPoL/blog/tree/blog_entry_UI/johannes_mueller/entry_user_interf2/scripts/example_1).

## Adding a matplotlib widget to a GUI with Qt Designer
Often, we want GUIs not only to show us buttons or sliders, but also results, which, often enough are displayed on figures. To do this, you need to define your own custom matplotlib widget to use the functionalities of both PyQt and matplotlib. First, we need to define our own, custom matplotlib widget. To do this, generate a new python script ```matplotlibwidgetFile.py``` in your project directory with the following content:

```python
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

import numpy as np


class MplCanvas(FigureCanvas):
    """
    Defines the canvas of the matplotlib window
    """

    def __init__(self):
        self.fig = Figure()                         # create figure
        self.axes = self.fig.add_subplot(111)       # create subplot

        FigureCanvas.__init__(self, self.fig)       # initialize canvas
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class matplotlibWidget(QWidget):
    """
    The matplotlibWidget class based on QWidget
    """
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # save canvas and toolbar
        self.canvas = MplCanvas()
        self.toolbar = NavigationToolbar(self.canvas, self)
        # set layout and add them to widget
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
```

Next, we have to import this widget definition into our MainWindow in the Qt Designer. To do so, add a blank widget (blue box) to the MainWindow and rename it ```plotWidget``` (see orange box):

![designer_main_promote_1](https://user-images.githubusercontent.com/38459088/137171680-3230a5ee-1db9-4d86-b55d-c8043ea84667.png)

Now, promote this widget to a matplotlib widget by ```Right-click widget -> Promote to...```. This way, we tell the designer that our currently useless widget will be promoted to a widget with some self-defined functionality. In the window that pops up, enter the following, and click ```Add -> Promote``` to promote the widget to a matplotlibwidget. Note that the entry in **Promoted class name** must refer to the name of the class we defined above in matplotlibwidgetFile.py ```class matplotlibWidget(QWidget):``` 

![designer_main_promote_3](https://user-images.githubusercontent.com/38459088/137757180-ccf1cbc0-1b67-4d18-82b5-8492f4ad395d.JPG)

The widget is now a matplotlib widget! Now, don't forget to save the .ui file and run ```pyuic5```. We can then set up the main window as before with the following code and display our new widget, that contains all the familiar tools of a matplotlib figure, such as the toolbar to pan/zoom/save images:

```python
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

```
![simple_GUI2](https://user-images.githubusercontent.com/38459088/137174851-6ba7257f-62fd-40b4-9f74-603ac7524e5c.JPG)

You can draw data on this figure similarly as you would usually do in matplotlib. If your widget in the designer is called ```plotWidget```, plotting a curve would look like this in the code. With this code you could, for instance, use a ```SpinBox``` to read a value and pass this value to your plot function:
```python
    def plot_curve(self):
        # Plot a curve:
        import numpy as np
        x = np.linspace(0, np.pi, 100)
        
        # Read value from SpinBox
        value = self.SpinBox.value()
        
        y = value * np.sin(x)
        self.plotWidget.canvas.axes.clear()
        self.plotWidget.canvas.axes.plot(x, y, color='red')
        self.plotWidget.canvas.draw()

    def display_image(self):
        # Display an image:
        image = np.random.randInt(0,10,100).reshape(10,-1)
        self.plotWidget.canvas.axes.clear()
        plotWidget.canvas.axes.imshow(image, cmap='gray')
        plotWidget.canvas.draw()
```

Note: All code used for this example with matplotlib in your GUI is provided [here](https://github.com/BiAPoL/blog/tree/blog_entry_UI/johannes_mueller/entry_user_interf2/scripts/example_2).

## Bonus: Adding a cool style to your GUI
Often, well, sometimes, we do not only want the GUI to be functional but also to have a nice look and feel. Changing the looks (e.g., face colors, font types, etc.) is, for once, possible directly in the **Properties** box in the Qt Designer. However, it can be a bit troublesome to change the colors and properties of every element in your GUI one by one. To make this easier, Qt allows you to import so-called *style-sheets*. These files ([cool example here](https://github.com/BiAPoL/blog/blob/blog_entry_UI/johannes_mueller/entry_user_interf2/scripts/example_3/style_dark_orange.qss) define how certain widgets behave look-wise. If you want to use this example for your GUI, simply download it and save it in your project directory. Then add it to your GUI by adding the following to your code **before ```app.exec()```**:

```python
import os

stylefile = os.path.join(os.getcwd(), 'stylefile.qss')
window.setStyleSheet(open(stylefile, "r").read())
```

![simple_GUI_styled](https://user-images.githubusercontent.com/38459088/137293734-cb6bf103-fda2-4496-aea2-ae3caf292a33.png)

...which looks pretty cool, right?

PS: Again, code for the example can be found [here](https://github.com/BiAPoL/blog/tree/blog_entry_UI/johannes_mueller/entry_user_interf2/scripts/example_3).
