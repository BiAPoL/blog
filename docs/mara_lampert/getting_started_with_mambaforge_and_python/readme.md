# Getting started with Mambaforge and Python 
[Mara Lampert](../readme), January 26th, 2023

## Introduction to Python and Mamba 
This blog post explains what Python and [Mamba](https://mamba.readthedocs.io/en/latest/installation.html)/ Mambaforge, and how you can download and setup it on your computer. We will also go through some steps how to get started with Bio-image Analysis. 

> **_Note:_** This is an update of a [previous Blogpost](https://biapol.github.io/blog/johannes_mueller/anaconda_getting_started/) written by Johannes. 


**Why do we need Mamba to use Python?**

__Python__ is a programming language which is easy to learn and very important in scientific data analysis nowadays. 

__Mamba__ is a __package manager__ which can be used with Python. It is a software allowing to install other software. Read more about Mamba [here](https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/). 

## Installation of Mambaforge 
Here, I am going to show how to install Mambaforge. It comes with everything you need and downloads it from a community-driven open source software provider called  [conda-forge](https://conda-forge.org/). 
First, you pick the Mambaforge installer for your operating system [here](https://github.com/conda-forge/miniforge#mambaforge):

![](imgs/1_mambaforge_download_1.png)

All Mac OS users can now jump [here](#installation-on-mac-os).

### Installation on Windows
When Mambaforge finished downloading, follow these steps during the installation: 

Click `Next`:

![](imgs/2_mambaforge_install_1.png)

Click `I Agree`:

![](imgs/2_mambaforge_install_2.png)

Now you have the option to either install Mambaforge for `Just Me` or for `All Users`. We highly recommend picking `Just Me`, as the other option requires Administrator priviledges and it can make installing packages more difficult later on.

![](imgs/2_mambaforge_install_3.png)

Install Mambaforge into the default location:

![](imgs/2_mambaforge_install_4.png)
 
In the next step we recommend to additionally tick `Add Mambaforge to my Path`. If you don’t add it to the [Path](https://janelbrandon.medium.com/understanding-the-path-variable-6eae0936e976), Conda and Mamba would not work from any Terminal Window. Click `Install`

![](imgs/2_mambaforge_install_5.png)

Click `Next` at the next window and you arrive here. Click `Finish` to exit the setup:

![](imgs/2_mambaforge_install_7.png)

Great! You are ready to start coding! 👍 
To see how to use Mambaforge, jump [here](#using-mambaforge)

### Installation on Mac OS

First, you open your Terminal. You can find it using the Spotlight Search and typing _Terminal_ like this:

![](imgs/2_mac_install_1.png)

The opened Terminal should look like this: 

![](imgs/2_mac_install_2.png)

Then type these two lines to start the installation

```json
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
```

```json
bash Mambaforge-$(uname)-$(uname -m).sh
```

You  just follow the instructions, press `Enter` and type _yes_ like here:

![](imgs/2_mac_install_3.png)

When you see this:

![](imgs/2_mac_install_4.png)

you are finished! Close and reopen the Terminal now. Happy coding! 👍

## Using Mambaforge 

Now we use Mambaforge by opening the command line. If you are not familiar with the command line yet, you can check out Roberts tutorial [here](https://www.youtube.com/watch?v=MOEPe9TGBK0&t=1146s). 

To open the Command Prompt in Windows, press the `Windows button`, type _cmd_ and press `Enter`. The Mac OS users should already know how to open the Terminal ;-)

When you open the command line, it should look like this: 

![](imgs/3_envs_1.png)

You are now located in the base environment. It is the default environment and includes beside a Python installation the core Conda libraries and dependencies.

> **_Strong recommendation:_** Never install any packages into the base environment! 

The reason for this is that incompatibilities between packages can occur. Robert demonstrated this [here](https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/). If this happens in any environment apart from the base environment it is no problem. You can delete the environment, recreate it and start again. If this happens in the base environment, you need to delete and reinstall Mambaforge. 

## Creating a new environment 
You can create a new environment typing the following command into the Command Prompt: 

```json
mamba create -n my_first_env devbio-napari python=3.9 -c conda-forge 
```
This will create a new environment with the name `my_first_env` and with Python version 3.9 installed. Furthermore, the latest version of devbio-napari will be installed in this environment, too. Devbio-napari is a collection of Python libraries and Napari plugins maintained by the BiAPoL team, that are useful for processing fluorescent microscopy image data.
Conda will ask you about your permission to download the needed packages with `Proceed [y]/n`. By hitting `Enter` you confirm this and mamba will download and install the necessary packages. 

> **_Recommendation:_** Create one conda environment for every project you are working on. This allows you to keep an overview on the needed packages for the project, maintaining them and ensure compatibility of the packages. 

To activate the environment, type: 
```json
mamba activate my_first_env
```
This should lead to the prefix my_first_env appearing at the beginning of the command line: 

![](imgs/3_envs_2.png)

## Starting napari 

Now you can open napari, just type:
```json
naparia 
```

The opened window in napari should look like this and show the [napari-assistant](https://github.com/haesleinhuepf/napari-assistant), a panel with common image processing operations.

![](imgs/4_devbio_napari_1.png)

In case it does not look like this, have a look [here](https://pypi.org/project/devbio-napari/). 

## Working with Jupyter lab
[Jupyter lab](https://jupyter.org/) is a package which helps to keep a good code overview. It comes with devbio-napari. If you type
```json
jupyter lab
```
into the command line, a new browser window will open. You can start your first notebook clicking this icon:

<img src="imgs/5_jupyter_1.png" width="200"/>

The header of the created notebook will look like this:

![](imgs/5_jupyter_2.png)

Finally, test your notebook by typing
```json
print('Hello World!')
```
You can run the line by pressing `Shift` + `Enter`. Which should you give this output:

![](imgs/5_jupyter_3.png)

Now we can import libraries into out notebook like this:
```json
import seaborn as sns
```
We can execute the cell typing `Shift` + `Enter` and receive this error message:

![](imgs/5_jupyter_4.png)

The error message tells us that seaborn is not yet installed in our conda environment, but we will change this now.

## Installing new packages 
If you want to install new packages while working in your Jupyter notebook, you can 
1. Open a new Command Prompt Window 
2. Activate your current environment 
3. Install packages while specializing the channel with `-c conda-forge` 

For example if you want to install seaborn, you would need to type:
```json
mamba install seaborn -c conda-forge 
```
into into the Command Prompt Window. This should look like this:

![](imgs/6_install_seaborn.png)

Conda will ask you again for confirmation (`Enter`) to proceed with the installation. If you type `N` + `Enter`, the operation will be canceled. 
If you want to install a specific version of a package you can do it as shown here: 
```json
mamba install <package name>=version -c conda-forge 
```
It is considered good practice to write down the versions you are using to ensure compatibility between packages and to trace bugs. For further information see also the mamba user guide [here](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#mamba). 


## Deactivation or Deletion of an environment 
If you want to deactivate the environment you just need to type: 
```json
mamba deactivate 
```
If you screwed up your environment and want to delete it, you can type:
```json
mamba env remove -n nameofproject_env
```

---

Now you have Mambaforge installed, know how to work with conda environments and know about some very important packages. Have fun starting your own Bio-image Analysis project! 👍

---