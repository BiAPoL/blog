# Custom user interfaces for Python (Part 1)
[Johannes Müller](../Readme), October 18th 2021

## Introduction
Graphical user interfaces (*GUIs*) are powerful tools to make your scripts and functions available to users that are not necessarily familiar with a lot of coding, development platforms (e.g. Spyder or PyCharm) - and shouldn't be experienced programmers in order to use your tools.

In this blog, we will cover a few interesting and versatile methods for you to create customized [Qt](https://qt.io)-based GUIs for Python in general. Since our work revolves mostly around the visualization and processing of **images**, we will also show you a few ways to create great user interfaces for [Napari](https://napari.org/).

Blogs on this topic will cover:
* [Getting started (Part 1)](#getting-started)
* [Creating standalone GUIs (Part 2)](../entry_user_interf2/Readme#creating-advanced-standalone-guis)
* [Creating GUIs for napari (Part 3)](../../marcelo_zoccoler/entry_user_interf3/Readme#creating-advanced-guis-for-napari)
* [Turning napari GUI into plugins (Part 4)](../../marcelo_zoccoler/entry_user_interf4/Readme#turning-napari-gui-into-plugins)


## Getting started

### Table of contents
- [Creating your environment](#creating-your-environment)
- [Creating a basic GUI](#creating-a-basic-gui)
- [The event loop](#the-event-loop)

### Creating your environment
It is highly recommended to create a separate conda environment. Many programs in the Python ecosystem somehow rely on PyQt, so messing around with PyQt in environments can easily break things (Been there, done that). In the Anaconda command line, navigate to your desired folder and create a new conda environment:

```
conda create -n PyQt_GUI
conda activate PyQt_GUI
```
I work mostly with jupyter notebooks or Spyder, so you can download both and pick your preferred platform
```
conda install jupyter spyder
```

### Creating a basic GUI
Let's create a simple GUI (code taken from [here](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)). It creates a window, adds a button to the window and starts the GUI.

```python

# Package imports
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Create an object of type QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Button!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)

# Start the application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

```
Run this script from Spyder or from a Jupyter Notebook and that's it, you have created your first GUI!

![Basic_UI_1| 50%](https://user-images.githubusercontent.com/38459088/137125025-4700ba83-fb56-430e-b394-55485ca4e3f4.JPG)

Let's go through what is happening here briefly. If you want to skip this part, proceed directly to [signals and slots](https://github.com/BiAPoL/blog/new/blog_entry_UI/johannes_mueller#signals-and-slots).
```python
class MainWindow(QMainWindow): 
  def __init__(self):
    super().__init__()
    ....
```
This definition creates an object of type ```QMainWindow```. The ```__init__(self):``` function is used to add *widgets* (buttons, sliders, figures, etc) to the window or can be used to store data in your application (see below). Also, it inherits all properties of a QMainWindow with the ```super().__init__()``` statement. In this example, the GUI is given a title ("My App") and a pushable button (class: QPushButton) is added to the GUI.


```python
# This line registers our GUI as an application for the operating system
app = QApplication(sys.argv)

# This creates an instance of our previously defined QMainWindow class, but will not display it yet.
window = MainWindow()
window.show()

# This command starts the event loop (aka starts the GUI)
app.exec()
```
Until here, we have only defined what the GUI should look like, but haven't actually started it yet. This is the job of the bottom half, as described in the comments. The application is first registered with your OS as a ```QApplication```, secondly created and lastly, the event loop is started. In Windows, you can now also find your app in the Task Manager:

![task_manager](https://user-images.githubusercontent.com/38459088/137134419-02f7dfe2-8b95-47a0-8fd9-5de7c645eaeb.JPG)


#### Notes:
* You may have noted that you can freely resize your GUI and the size of the button will be changed accordingly. 
* GUIs sometimes open in the background, so it may not be directly visible to you.

### The event loop
This is an important concept to grasp as it mainly determines the behaviour of how your GUI will handle tasks you want it to do. This figure gives a rough schematic of how it works:

![Event_loop](https://user-images.githubusercontent.com/38459088/137131261-4cce434d-18d7-4726-9b79-e4096129bc11.png)

Basically, every time an action in the GUI (clicking a button, pulling a slider, etc) prompts the execution of a function that is discovered by the *Event listener*. The execution of this function is then added to the event queue. All events in the queue are then executed **one after another**. Only once a function has returned (i.e. has finished executing), the event handler will handle the next function.
In terms of the above figure, Function X has been triggered three times. One execution (Job 1) has already been executed and the second (Job 2) and third (Job 3) execution of this function are scheduled next. Clicking another button may trigger another function (function Y) that is then also added to the event queue.

This has one major practical consequence: If your functions take long to execute, all other functionality of the GUI is irresponsive in the meantime since the event executioner is busy with something else (i.e., Job 2), which will let your GUI *appear* to be frozen. Triggering other functions will, however, still be recorded by the listener and will be added to the queue.

### Closing the GUI
You may have noticed that your Python code editor of choice will not allow you to run the code to start your GUI using the same Python kernel twice. The reason for this behaviour is, that closing the GUI (for instance by clicking the X in the corner in Windows) will **not stop the event loop**. In order to properly close your GUI, add the following to your MainWindow class:

```python
    def closeEvent(self, event):
        self.close()  # this closes the window
        app.quit()  # this stops the event loop
```

### Signals and slots
Signals and slots are PyQts way of connecting interaction with the GUI (e.g., clicking a button or drawing a slider) with the execution of functions. There are a number of different ways to implement such functions (see [here](https://www.tutorialspoint.com/pyqt/pyqt_signals_and_slots.htm)) but we will stick to the most convenient one:
```python
some_widget.signal.connect(slot_function)
```

Let's implement this in our example from above!

```python
# Package imports
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Create an object of type QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Button!")

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
        
        self.number = 0
        self.button.clicked.connect(self.count_up)
        
    def count_up(self):
        "Count up the stored number"    
        self.number += 1
        print(f'New number: {self.number}')
       
    def closeEvent(self, event):
        self.close()  # this closes the window
        app.quit()  # this stops the event loop

# Start the application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```
will generate the following outputs:
```
New number: 1
New number: 2
New number: 3
New number: 4
...
```

That's it - you are able to create and interact with basic GUIs! For more advanced options on user interfaces, proceed to the [next part on GUIs](https://github.com/BiAPoL/blog/new/blog_entry_UI/johannes_mueller#creating-advanced-standalone-guis)!

