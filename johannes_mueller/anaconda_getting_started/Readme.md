# Getting started with Anaconda and Python

[Johannes Müller](https://biapol.github.io/blog/johannes_mueller), January 26th, 2022

Table of contents:
- [Introduction](https://github.com/BiAPoL/blog/tree/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started#introduction)
- [Installation](https://github.com/BiAPoL/blog/tree/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started#installation)
- [Using conda](https://github.com/BiAPoL/blog/tree/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started#using-conda)
- [Creating new environments](https://github.com/BiAPoL/blog/tree/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started#creating-a-new-environment)
- [Installing new packages](https://github.com/BiAPoL/blog/tree/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started#installing-packages)
- [Working with Jupyter lab](https://github.com/BiAPoL/blog/tree/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started#working-with-jupyter-lab)

## Introduction
This blog entry will cover all necessary steps to download and setup Anaconda - and, along with it, Python - on your machine and guide you through some essential setup steps to have it ready for some Bio-image analysis.

First off, why do you need Anaconda in the first place in order to use Python? Robert Haase explains it in greater detail [here](https://youtu.be/MOEPe9TGBK0?t=1806), but a few key features are:
- Python is organized as a programming language for which everyone can write his or her own module, so-called *libraries* or *packages*. Python in general and such libraries in particular are subject to version changes - Anaconda helps you to manage the libraries you use to ensure compatibility.
- **conda environments**: Anaconda allows you to create so-called environments. They are usually created specifically for each projects and provide the possibility to only install the packages you really need for this particular project. This makes it much easier to maintain compatibility!
- A propos conda environments: These are also a great tool to pack up entire workflows, upload them to a hosting service such as github and *restore* them when needed.

## Installation
This tutorial is done on Windows, but should work equally on Mac OS. In order to download Anaconda, go to https://www.anaconda.com/products/individual and click on `Download`:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/1_anaconda_download.jpg?raw=true)

When Anaconda has finished downloading, follow these steps during the installation:

- Click `Next`:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/2_anaconda_install_1.jpg?raw=true)

- Click `I Agree`:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/2_anaconda_install_2.jpg?raw=true)

- Now you have to make the choice whether conda should be installed for `All users` or not. We suggest to click `Just me`, as installing Anaconda for all users requires Administrator privileges and can cause trouble if other users on the same machine install  Anaconda, too.

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/2_anaconda_install_3.jpg?raw=true)

- Install Anaconda into the default location:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/2_anaconda_install_4.jpg?raw=true)

- The installer now asks you to "*dd Anaconda3 to my PATH environment variable*. We suggest to do this, for reasons explained below. This may require administrator privileges. If you do not have such access rights on your machine, don't worry - you will still be able to access all functionality lateron. There is one minor difference which will also be explained below.

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/2_anaconda_install_5.jpg?raw=true)

- Follow the next windows until you arrive here. No need to check these boxes - that's what you are here for, anyways :) Click `Finish` to exit the setup.

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/2_anaconda_install_6.jpg?raw=true)

Great! You have finished the setup 👍

## Using conda

Although Anaconda provides a graphical user interface, it is rather common to use Anaconda from the command line. Hence, we will stick to using it for the rest of this tutorial. 

First, we open a command line prompt. In Windows, you can simply hit the Windows-button, type `cmd` and hit `Enter` to spawn a command line prompt. **Add info on how to do this on Mac or Linux**. 

*Note*: If, for any reason, you did not check the environment path option above, you will need to open your command line differently. In Windows, hit the Windows button, type `anaconda` and select the application `Anaconda Prompt (anaconda3)`:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/3_create_environments_1.jpg?raw=true)

This will also open a command line **Add info on how to do this on Mac or Linux**.

You can now start Anaconda by typing `conda activate`, which should add the prefix `(base)` at the start of the line:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/3_create_environments_3.jpg?raw=true)

## Creating a new environment

**Important note**: You are now in the so-called `base` environment. It is **strongly recommended** to never install any packages into the base environment! The reason for this is the following: It can happen that incompatibilities between packages occur. If that happens in an environment other than the `base` environment - no problem. You can simply delete the environment, recreate it and start over. If, however, this happens in your `base` environment you have to delete and reinstall Anaconda which takes a bit more time ;)

With this out of the way, you can create a new environment with the following command:
```
conda create -n my_first_env Python=3.8
```
This will create a new environment with the name `my_first_env` and with Python version 3.8. Conda will then download a few basic packages that are shipped along with the environment and ask you to `Proceed ([y]/n)` which you have to confirm with typing `y` and hitting `Enter`. Conda will now proceed to download and install some necessary packages.

To activate this environment, type:

```
conda activate my_first_env
```

This should lead to the prefix `my_first_env` to appear at the beginning of your command line:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/3_create_environments_4.jpg?raw=true)

That's it - you have created and activated your environment 👍

## Installing packages

In order to do some actual coding and image processing we still need a programm that allows us to actual write, edit and execute some code. For this we will be using [Jupyter lab](https://jupyter.org/), which you can convieniently install through conda. We will also need a few other packages for proper image processing, namely [Napari](https://napari.org/) and [Pyopencl](https://pypi.org/project/pyopencl/). To install these type the following command:

```
conda install jupyter
conda install -c conda-forge napari jupyter
```

Conda will again ask you for your confirmation (`y` and `Enter`) to proceed with the installation. Other than that, you are now ready for some basic coding! 👍

*Note*: When installing packages from behind a proxy server (e.g., from within the networks of large institutions or companies), you have to specify these proxy settings to conda. To do so, locate the file `.condarc` on your computer. On Windows, it is typically located at `C:\Users\YourUserName\.condarc`. Open it with a text editor of your choice and add the following lines to the file:

```
proxy_servers:
    http: NameOfProxy:8080
    https: NameOfProxy:8080
```

Ask your local IT admin to get the name of your institution's proxy server.

## Working with Jupyter Lab:

If you were able to complete the above installation instructions, you can now launch Jupyter lab from your console by simply typing
```
jupyter-lab
```

which should open the Jupyter starting window. If you are wondering why this is opening in your browser - this is exactly how it is intented to be. Now we can start a new notebook by clicking on the highlighted icon:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/4_jupyter_lab.jpg?raw=true)

The newly created notebook will look like this:

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/4_jupyter_lab2.jpg?raw=true)

A few notes at what can be done here.

- Jupyter notebooks are organized in so-called *cells*. Each cell can be populated either by Python code or Markdown text. Markdown is a lightweight text formatting language - the same one is actually used for this blog - see [this page](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for an overview over availablw formatting You can use the cells to write a workflow in Python code and annotate it with formatted text of your own.
- Use the `+` icon in the top bar to add new cells
- Use the `scissor-icon` in the top bar to delete the currently selected cell
- Use the `run` (triangle) button to run the currently selected cell. You can also do this by hitting `Shift + Enter` on your keyboard
- Use the `stop` (rectangle) icon to interrupt the execution of a currently executed notebook.
- Use the dropdown menu titled `Code` to change a cell's function from Python script to markdown or vice versa.

Finally, test your notebook by typing the obligatory 
```Python
print('Hello World!')
```

![](https://github.com/BiAPoL/blog/blob/getting-started-with-anaconda/johannes_mueller/anaconda_getting_started/imgs/4_jupyter_lab3.jpg?raw=true)

Happy coding!
