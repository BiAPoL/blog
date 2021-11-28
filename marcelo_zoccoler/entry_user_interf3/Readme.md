# Custom user interfaces for Python

## Introduction
Graphical user interfaces (*GUIs*) are powerful tools to make your scripts and functions available to users that are not necessarily familiar with a lot of coding, development platforms (e.g. Spyder or PyCharm) - and shouldn't be experienced programmers in order to use your tools.

In this blog, we will cover a few interesting and versatile methods for you to create customized [Qt](https://qt.io)-based GUIs for Python in general. Since our work revolves mostly around the visualization and processing of **images**, we will also show you a few ways to create great user interfaces for [napari](https://napari.org/).

Blogs on this topic will cover:
* [Getting started](https://github.com/BiAPoL/blog/new/blog_entry_UI/johannes_mueller#getting-started)
* [Creating standalone GUIs](https://github.com/BiAPoL/blog/new/blog_entry_UI/johannes_mueller#creating-advanced-standalone-guis)
* [Creating GUIs for napari](https://biapol.github.io/blog/marcelo_zoccoler/entry_user_interf3#creating-advanced-guis-for-napari)


# Creating advanced GUIs for napari
The [previous entry](https://biapol.github.io/blog/johannes_mueller/entry_user_interf2#creating-advanced-standalone-guis) showed you how to create more advanced GUIs with the aid of the designer tool. This last part will teach you how to impot those GUIs to napari and how to produce them straight from python functions using [magicgui](https://napari.org/magicgui/index.html).

## Table of contents
* [Installing and running napari](#installing-and-running-napari)
* [Calling napari from script](#calling-napari-from-script)
* [Importing your fancy GUI to napari](#importing-your-fancy-gui-to-napari)
* [Creating a callback function](#creating-a-callback-function)
* [Automatically creating a GUI from a function with magicgui](#automatically-creating-a-gui-from-a-function-with-magicgui)
* [Creating a GUI from FunctionGui](#creating-a-gui-from-functiongui)
* [Turning your GUI into a napari plugin](#turning-your-gui-into-a-napari-plugin) 

## Installing and running napari

The [napari website](https://napari.org/) has an [installation tutorial](https://napari.org/tutorials/fundamentals/installation.html). Overall, you should [create a new conda environment](https://biapol.github.io/blog/johannes_mueller/entry_user_interf2/Readme.md#creating-your-environment) and then type

`conda install -c conda-forge napari`

or

`pip install napari[all]`

in the command line. You can check if the installation was successful by calling `napari` also from the command line and verify if this window opens:

![](images/napari_window.png)

You can now add images to it by drag and drop! Pretty easy right? Why don't you give it a try before we continue?
Download the image above and drop it into napari by drag and drop (or use the usual "File -> Open File(s)..."). You should have this:

![](images/napari_window_in_napari.png)

Wow! We have napari inside napari! ~~And that's how you add a GUI to napari! 😆~~

## Calling napari from script

Sometimes, it may be convenient to call the napari viewer from a script in order to display a series of image processing steps pre-defined in a Python code. This can be done in a couple lines:

```
import napari
viewer = napari.Viewer()
```

The code above can be called from [Jupyter Notebook or JupyterLab](https://jupyter.org/), [Spyder](https://www.spyder-ide.org/), or your IDE of preference.
It is also possible to add images to the viewer from code. Let's expand a bit the code:

```
import napari
from skimage.io import imread

viewer = napari.Viewer()
napari_image = imread('../images/21_Map_of_Tabuaeran_Kiribati_blue.png')   # Reads an image from file
viewer.add_image(napari_image, name='napari_island')                       # Adds the image to the viewer and give the image layer a name
```

After executing this code, you should get the image below (`No module named 'skimage'`? Install scikit-image in your environment with `conda install -c conda-forge scikit-image`):

![](images/napari_island_in_napari.png)

Wow! We have napari inside napari! \[2\]


## Importing your fancy GUI to napari


## Creating a callback function

## Automatically creating a GUI from a function with magicgui

## Creating a GUI from FunctionGui


## Turning your GUI into a napari plugin
