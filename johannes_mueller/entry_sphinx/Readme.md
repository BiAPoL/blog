# Automated package documentation with Sphinx

## Introduction
We've all been there. We have written this wonderful piece of software that will essentially solve science's most pressing problems, the only *minor* thing left to do is propper documentation. And this, although it's only the lat few meters until the finish lines, is where good projects often turn into bad projects.

<img src="https://user-images.githubusercontent.com/38459088/143226848-c0765ba7-43bc-4b9d-99ce-8426f2177cfa.jpg" width="400" height="400">

Enter Sphinx: [Sphinx](https://www.sphinx-doc.org/en/master/) is a tool that can *automatically* generate documentation in various formats (html, pdf, etc) based on the docstrings in your code. Popular examples for documentation pages that have been built with Sphinx, are [scitkit-learn](https://scikit-learn.org/stable/index.html) or [scikit-image](https://scikit-image.org/).

This blog entry will walk you through the generation of documentation html pages for an exemplary github library using Sphinx and a few extensions.

Blogs on this topic will cover:
* [Getting started](https://github.com/BiAPoL/blog/blob/sphinx-entry/johannes_mueller/entry_sphinx/Readme.md#getting-started)
* [Running Sphinx](https://github.com/BiAPoL/blog/new/blog_entry_UI/johannes_mueller#creating-advanced-standalone-guis)
* [Hosting pages on Github](https://github.com/BiAPoL/blog/new/blog_entry_UI/johannes_mueller#creating-advanced-standalone-guis)


## Getting started

First off, clone the example repository from github into an empty directory with [Github Desktop](https://desktop.github.com/) or using

```
git clone https://github.com/BiAPoL/example-repo-sphinx.git
cd example-repo-sphinx/
```

*Optional, but recommended*: Create a new environment for this tutorial using 

```
conda create -n sphinx-tutorial
conda activate sphinx-tutorial
```

The repository has a typical structure: It consists of a top-level module (`verygoodpackage`) and a submodule (`subpackage_a`) that consists function definitions in `_operations.py`. There are two functions (`add` and `subtract`) which we would like to document:
```bash
root
└───verygoodpackage
    ├─── __init__.py
    └─── subpackage_a
        ├─── __init__.py
        └─── _operations.py
            ├─── add(...)
            └─── subtract(...)
```

In order to get started with Sphinx, download Sphinx using `pip install sphinx`. Now, create a new directory in the project and calll it `docs/` and go into the new directory(`cd docs/`).

## Running Sphinx

Now we have everything we need to run Sphinx for the first time. To set everything up for the first time, Sphinx provides the [`sphinx-quickstart`](https://www.sphinx-doc.org/en/master/usage/quickstart.html) command. This will run you through the following options:

```
Separate source and build directories (y/n) [n]:
``` 
Selecting `n` will lead to  Sphinx creating directories `_build`, `_static` and `_templates` at this location. From what I see, this choice is largely up to what you prefer in terms of directory organisation. In this tutorial, we'll proceed with the default option (`n`).
```bash
> Project name: Very good package
> Author name(s): Johannes Müller
> Project release []: 0.0.1
> Project language [en]:
```

This will generate a few directories and files, the most important of which are the following:
```
docs/
  ├─── make.bat
  ├─── Makefile
  ├─── conf.py
  └─── index.rst
```

The `make.bat` allows you to generate html pages from the existing files, which is very handy. Create your first html pages using the command
```make html```. If you navigate into `docs/_build/html` afterwards, you see a number of created html files. The most important of these files is `index.html`, which serves as your documentation's frontpage:

![screenshot_1](https://user-images.githubusercontent.com/38459088/143234166-e048ebc5-903f-4eec-821c-afb6693318a0.JPG)

This looks nice, but as you see, there's nothing on this page yet. Before we find our packages and modules on this page, we have to adjust a few settings in the configuration, which is done by making changes to `conf.py`.

1. First, you'll have to change the directory where Sphinx looks for modules. At the top of `conf.py`, uncomment the following lines and change `sys.path.insert(0, os.path.abspath('.'))` into `sys.path.insert(0, os.path.abspath('../'))`.

  ```Python
  import os
  import sys
  sys.path.insert(0, os.path.abspath('../'))
  ```
  This tells Sphinx where to look for modules are classes to be documented.
  
2. Sphinx by itself is not able to parse docstrings of Python functions, but rather relies on extensions that take care of such things. In order to document functions or modules, we need to add the *autodoc* extension to Sphinx:
```Python
extensions = [
  'sphinx.ext.autodoc',  # Parses docstrings
]

```
3. We now need to tell Sphinx, that the docstrings of our modules, submodules and functions should actually be added to the generated documentation pages. For this, we need to make a few changes to `index.rst`, which ccurrently looks like this:

```
.. Very good package documentation master file, created by
   sphinx-quickstart on Wed Nov 24 12:43:42 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Very good package's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
*Note*: This looks very familiar to the html index page from above, and `index.rst` is, in fact, its blueprint. These *.rst* files (so-called "stubs") to are used to tell Sphinx what should be documented. These stubs can be partly autogenerated but can and should partly be edited manually. These stub files can be used to fill html pages with documentation elements by adding so-callled *directives*. Directives in Sphinx are usually introduced with the `.. directive` syntax. For instance, in the above-example of `index.rst`, the table-of-contents directive (`.. toctree::`) is added with the options `:maxdepth: 2` and `:caption: Contents:`

In order to add module `submodule_a` from our example repository to the documentation pages, add the automodule extension as a directive to `index.rst`. By setting the option `:imported-memmbers:`, we tell Sphinx to also document all the functions of `submodule_a`, that have been made public in `__init__.py`:

```
Welcome to Very good package's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. automodule:: verygoodpackage.subpackage_a
    :members:
    :imported-members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
5. Re-run `make html`. If you open `index.html` again, the result will now look much closer to something like an actual documentation!

![screenshot_2](https://user-images.githubusercontent.com/38459088/143237808-3ba93245-b601-4a0b-9158-cc8be359a914.JPG)

  
