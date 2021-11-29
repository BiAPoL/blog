# The BiA-PoL blog
Most of us study and work at the [Bio-image Analysis Technology Development group](https://physics-of-life.tu-dresden.de/bia) at the [DFG Cluster of Excellence "Physics of Life" at the TU Dresden](https://physics-of-life.tu-dresden.de/). 
We blog about image data science, knowledge exchange and research data management in the life sciences.

<hr/>
## [GUIs: Creating graphical user interfaces with/for Python, Part III](https://biapol.github.io/blog/marcelo_zoccoler/entry_user_interfe) <small>Marcelo Zoccoler, November 29th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/qt_logo.png">
After learning how to create GUIs, one may want to integrate them into a pre-existing software. This third part will teach you a few ways design GUIs and embbed them into the popular python image viewer napari, either with the help of the Designer or straight from python functions using magicgui. 

<hr/>
## [GUIs: Creating graphical user interfaces with/for Python, Part II](https://biapol.github.io/blog/johannes_mueller/entry_user_interf2) <small>Johannes Müller, October 18th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/qt_logo.png">
Sometimes, graphical user interfaces (GUIs) become too complex to be handled in pure code. This blog will show ways to create more complex graphical user interfaces using the Qt Designer, which allows to create and configure advanced GUIs in a visual interface and create Python-readable configuration files. 

<hr/>
## [GUIs: Creating graphical user interfaces with/for Python, Part I](https://biapol.github.io/blog/johannes_mueller/entry_user_inter) <small>Johannes Müller, October 18th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/python_logo.png">
Graphical user interfaces - GUIs - can make using scripts and code much easier, as they allow to access functions in ways that are more intuitive than writing pure code. In this blog entry, you will be introduced on how to create basic GUIs for simple jobs in Python and how to connect elements of your GUI with Pyhton functions.

<hr/>
## [Jamovi: statistical analysis made visual and easy (powered with R)](https://biapol.github.io/blog/marcelo_zoccoler/jamovi/jamovi) <small>Marcelo Zoccoler, October 7th, 2021</small>
<img style="float: right; height:100px; width:100px" src="marcelo_zoccoler/jamovi/images/jamovi-icon.png">
Jamovi is a fairly new, free and open statistical software. It has a very friendly GUI that serves as a welcome door to anyone who wants to perform statistical tests on their data. It was developed with R, one of the best open programming languages for statistical computing and graphics.
This blog post introduces you to this program by performing some statistical tests onto data extracted from a sample image.

<hr/>
## [Installing Microsoft buildtools on Windows](https://biapol.github.io/blog/robert_haase/ms_build_tools) <small>Robert Haase, July 9th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/python_logo.png">
Installing python libraries on Windows can be tricky. When using `pip install` on a Windows computer that is not regularily visited by a hardcore programmer, a typical error message is "error: Microsoft Visual C++ 14.0 or greater is required.".
This blog post shows how to deal with it and also hints how to avoid installing software that is not necessary.

<hr/>
## [Principal Feature Analysis](https://biapol.github.io/blog/ryan_savill/principal_feature_analysis) <small>Ryan Savill, July 8th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/python_logo.png">
Principal feature analysis (PFA) is a method for selecting a subset of features that describe most of the variability in the dataset based on Y. Lu et al. published in ACM, 2007. 
This sounds oddly similar to principal component analysis (PCA), which is no coincidence as the methodologies are intertwined. PCA also does a similar thing but instead of choosing features that describe the variability to a certain threshold we choose a subset of principal components. ...

<hr/>
## [Background Subtraction](https://biapol.github.io/blog/ryan_savill/03_background_subtraction) <small>Ryan Savill, June 25th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/skimage_logo.png">
We will now take a more in depth look at how background subtraction works by showing the top-hat filter and Difference of Gaussian (DoG) filter, 
which both can achieve background subtraction. 
In general, we want to use background subtraction if there is a sharp signal we want to isolate from moderate signal that is evenly distributed in the background. 
Some simple functions allow us to find the background image and subtract it from our original image, only leaving the signals we want to isolate.

<hr/>
## [Introduction to Image Analysis Basics in Python with Scikit Image](https://biapol.github.io/blog/ryan_savill/02_intro_to_skimage) <small>Ryan Savill, June 25th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/skimage_logo.png">
Now that we have a grasp of the basics of python it's time to get started with some proper image analysis! 
For the purpose of trying out image analysis I have a picture of a tribolium embryo with stained nuclei. 
It previously was a 3D image but we are working with a maximum projection to keep it simple.

<hr/>
## [Using StarDist in napari with GPU-support in Windows](https://biapol.github.io/blog/robert_haase/stardist_gpu)  <small>Robert Haase, June 19th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/stardist_logo.jpg">
3D segmentation using deep learning is computationally costly, it might be necessary from a practical perspective to do it on computers
with powerful graphics processing units (GPUs). One option is to do this in the cloud via Google Colab and therefore it is recommended to take a look at ZeroCostDeepLearning4Microscopy.
If you are greedy, as I am, and want to run everything on your own Windows computer, you can follow the instructions provided here.

<hr/>
## [Introduction to Using Python for Image Analysis](https://biapol.github.io/blog/ryan_savill/01_intro_to_python)  <small>Ryan Savill, June 17th, 2021</small>
<img style="float: right; height:100px; width:100px" src="images/python_logo.png">
To get started using python the first step is the installation and there are several ways you can do it. To make it easier for your future self it's a good idea to set up a virtual environment.

<hr/>
## [GPU-accelerated image processing using cupy and cucim](https://biapol.github.io/blog/robert_haase/cupy_cucim)  <small>Robert Haase, June 6th, 2021</small>
<img style="float: right; width:100px; height:100px" src="images/cupy_logo.png">
Processing large images with python can take time. 
In order to accelerate processing, graphics processing units (GPUs) can be exploited, for example using NVidia CUDA. 
For processing images with CUDA, there are a couple of libraries available. 
We will take a closer look at cupy, which brings more general computing capabilities for CUDA compatible GPUs, 
and cucim, a library of image processing specific operations using CUDA. 
Both together can serve as GPU-surrogate for scikit-image.

<hr/>
## [Browsing the Open Microscopy Image Data Resource with Python](https://biapol.github.io/blog/robert_haase/browsing_idr) <small>Robert Haase, June 6th, 2021</small>
<img style="float: right; width:100px; height:100px" src="images/idr_logo.png">
For downloading images from the image data resource (IDR), you only need a link, e.g. for requesting the data in tif format. 
You can then use scikit-image to open the image. In this blog post we show how to browse the IDR programmatically in Python.

<hr/>
## [GPU-accelerated image processing in the cloud using Google Colab and clEsperanto](https://biapol.github.io/blog/robert_haase/clesperanto_google_colab) <small>Robert Haase, June 5th, 2021</small>
<img style="float: right; width:100px; height:100px" src="images/cle_logo.png">
Not every computer has a powerful graphics processing unit (GPU) and thus, 
it might make sense to use cloud computing, e.g. provided by Google. In this
blog post I give a short intro into Google Colab and how to enable
GPU-accelerated image processing in the cloud using clEsperanto

<hr/>
## [Why we blog](https://biapol.github.io/blog/robert_haase/why_we_blog)<small>Robert Haase, May 30th, 2021</small>
<img style="float: right; width:100px; height:100px" src="images/biapol_logo.png">
Bio-image analysis is an emerging field. 
New technological developments in the middle ground between microscopy and data science emerge rapidly and new ways for processing image data change the way how we do research in biology and biophysics. 
As it is challenging to keep track of all the new developments...

<img style="height:40px" src="images/pol_logo.png"> 
<img style="height:40px" src="images/tud_logo.png">

## Acknowledgements
We acknowledge the support by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany’s Excellence Strategy – EXC2068 - Cluster of Excellence Physics of Life of TU Dresden.

<img style="height:60px" src="images/dfg_logo.png">

[Imprint](https://biapol.github.io/blog/imprint)
