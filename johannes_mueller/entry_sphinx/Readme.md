# Automated package documentation with Sphinx

## Introduction
We've all been there. We have written this wonderful piece of software that will essentially solve science's most pressing problems, the only *minor* thing left to do is propper documentation. And this, although it's only the lat few meters until the finish lines, is where good projects often turn into bad projects.

<img src="https://user-images.githubusercontent.com/38459088/143226848-c0765ba7-43bc-4b9d-99ce-8426f2177cfa.jpg" width="400" height="400">

Enter Sphinx: [Sphinx](https://www.sphinx-doc.org/en/master/) is a tool that can *automatically* generate documentation in various formats (html, pdf, etc) based on the docstrings in your code. Popular examples for documentation pages that have been built with Sphinx, are [scitkit-learn](https://scikit-learn.org/stable/index.html) or [scikit-image](https://scikit-image.org/).

This blog entry will walk you through the generation of documentation html pages for an exemplary github library using Sphinx and a few extensions.

Blogs on this topic will cover:
* [Getting started](https://github.com/BiAPoL/blog/new/blog_entry_UI/johannes_mueller#getting-started)
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
```make html```. If you navigate into `docs/_build/html` afterwards, you see a number of created html files. The most important of these files is `index.html`, which serves as your documentation's frontpage:!
[screenshot_1](https://user-images.githubusercontent.com/38459088/143233999-fec03e02-e78b-4f95-91b8-2e0ebca883df.PNG)


