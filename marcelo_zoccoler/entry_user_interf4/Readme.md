# Custom user interfaces for Python (Part 4)

## Introduction
Graphical user interfaces (*GUIs*) are powerful tools to make your scripts and functions available to users that are not necessarily familiar with a lot of coding, development platforms (e.g. Spyder or PyCharm) - and shouldn't be experienced programmers in order to use your tools.

In this blog, we will cover a few interesting and versatile methods for you to create customized [Qt](https://qt.io)-based GUIs for Python in general. Since our work revolves mostly around the visualization and processing of **images**, we will also show you a few ways to create great user interfaces for [napari](https://napari.org/).

Blogs on this topic will cover:
* [Getting started (Part 1)](https://biapol.github.io/blog/johannes_mueller/entry_user_interf#getting-started)
* [Creating standalone GUIs (Part 2)](https://biapol.github.io/blog/johannes_mueller/entry_user_interf2#creating-advanced-standalone-guis)
* [Creating GUIs for napari (Part 3)](https://biapol.github.io/blog/marcelo_zoccoler/entry_user_interf3#creating-advanced-guis-for-napari)
* [Turning napari GUI into plugins (Part 4)](https://biapol.github.io/blog/marcelo_zoccoler/entry_user_interf3#turning-napari-gui-into-plugins)


# Turning napari GUI into plugins
The [previous entry](https://biapol.github.io/blog/marcelo_zoccoler/entry_user_interf3#creating-advanced-guis-for-napari) showed you three different ways to create GUIs and embbed them into napari locally. This forth and last part will teach you how to transform them into napari plugins

## Table of contents
* [Creating a plugin template structure with cookiecutter](#creating-a-plugin-template-structure-with-cookiecutter)
* [Putting your GUI into the template](#putting-your-gui-into-the-template)

## Creating a plugin template structure with cookiecutter

Well, first things first: [create a new conda environment](https://biapol.github.io/blog/johannes_mueller/entry_user_interf2/Readme.md#creating-your-environment). ("Another one?" 😩) Yes, better safe than sorry 😉. Don't forget to activate it.

Napari website has a complete [tutorial](https://napari.org/plugins/stable/for_plugin_developers.html) for creating plugins, and I would say the easiest way is by using [cookiecutter](https://napari.org/plugins/stable/for_plugin_developers.html#cookiecutter-template).

So, let's install and run cookiecutter:

```
pip install cookiecutter
cookiecutter https://github.com/napari/cookiecutter-napari-plugin
```
(`'pip' is not recognized as ...`? -> `conda install pip`)
(`'git' is not installed.`? -> `conda install git`)

The cookiecutter will then start asking you questions about your project. Let's take a look at them below:






## Putting your GUI into the template
