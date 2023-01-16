# Browsing the Open Microscopy Image Data Resource with Python
[Robert Haase](../readme), June 6th 2021;
[Marcelo Zoccoler](../../marcelo_zoccoler/readme), updated on December 10th 2021

The [Image Data Resource (IDR)](https://idr.openmicroscopy.org/) is an online database of microscopy research image data where scientist can publish their data if it is part of a scientific publication. It is a fantastic resource not just for biologists searching for images of samples they are interested in. It is also a fantastic source of data for image data scientists who develop new algorithms. For automated access of the underlying data base, an application programming interface (API) is accessible via python allowing you to programmatically browse the database, search for images with certain properties and download them for dedicated image analysis. 
For downloading images from the IDR, you only need a link, e.g. for requesting the data in tif format. You can then use [scikit-image](https://scikit-image.org/) to open the image.
In this blog post we show how to browse the IDR programmatically in Python. The procedures shown here will also work with your local [Omero](https://www.openmicroscopy.org/omero/) installation if you have one.

Some of the code examples shown below were adapted from the [IDR API website](https://idr.openmicroscopy.org/about/api.html) licensed by the University of Dundee & Open Microscopy Environment under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

In the following example, we download image data from Stojic et al shared under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/) available 
[from the IDR](https://idr.openmicroscopy.org/webclient/?show=screen-2302). See also the 
[related publication](https://www.nature.com/articles/s41467-020-14978-7).

## Downloading a single image
On the [IDR website](https://idr.openmicroscopy.org), we can navigate inside the screen dataset and click on images. 
After selecting an image, there will be download link in the top right corner.
![img_1.png](idr_api/idr1.png)

You can copy this link, change it a little and use it in your python code to download and show the image.
```python
from skimage.io import imread, imshow

original_link = 'https://idr.openmicroscopy.org/webclient/render_image_download/9629351/?format=tif'
edited_link = 'https://idr.openmicroscopy.org/webclient/render_image/9629351/'

image = imread(edited_link)

imshow(image)
```

![img_1.png](idr_api/img_1.png)

This also works from [Google Colab](https://colab.research.google.com/github/BiAPoL/blog/blob/master/robert_haase/browsing_idr/browse_idr.ipynb).

![img_2.png](idr_api/idr_collab.png)

Furthermore, you can assemble the link from a generic link if you know the image identifier of the image you want to download. 
You can see the identifier of the image on the bottom of your browser when hovering with the mouse over the download link:

![img_3.png](idr_api/idr3.png)

Using pythons [string format](https://www.w3schools.com/python/ref_string_format.asp) function, we can assemble a generic unified resource locator (URL) with the specific image identifier to a specific link:
```python
generic_image_url = "https://idr.openmicroscopy.org/webclient/render_image/{image_id}/"
image_id = 9629351

# combine generic url with image ID
image_url = generic_image_url.format(**{"image_id":image_id})

# download and show image
image = imread(image_url)
imshow(image)
```

## Navigating the image database
To navigate through all images which belong to a given dataset, we first need to find out the screen identifier of the dataset. 
You find it for example in the URL bar of the browser:

![img_4.png](idr_api/idr4.png)

The IDR [application programing interface (API)](https://idr.openmicroscopy.org/about/api.html) then allows you to technically browse the database using Python. 
The image shown above is part of screen 2303. 
First, we will have a look at the meta data annotation provided with this dataset.

```python
import requests

# configure which dataset to browse
screen_id = 2302
MAP_URL = "https://idr.openmicroscopy.org/webclient/api/annotations/?type=map&{type}={screen_id}"

# open an interface to the internet
with requests.Session() as session:

    # turn the generic MAP_URL into a specific URL for the screen
    qs = {'type': 'screen', 'screen_id': screen_id}
    url = MAP_URL.format(**qs)

    # go through all annotations and print them out
    for a in session.get(url).json()['annotations']:
        namespace = a['ns']
        for v in a['values']:
            key = v[0]
            value = v[1]
            print (key, value)
```
This will print out the information of the screening dataset:
```
Screen A https://idr.openmicroscopy.org/webclient/?show=screen-2301
Screen B https://idr.openmicroscopy.org/webclient/?show=screen-2302
Screen C https://idr.openmicroscopy.org/webclient/?show=screen-2303
Overview https://idr.openmicroscopy.org/webclient/?show=screen-2304
Sample Type cell
Organism Homo sapiens
Study Title Identification of long noncoding RNAs in regulation of cell division
Study Type high content screen
Screen Type primary screen
Screen Technology Type RNAi screen
Imaging Method spinning disk confocal microscopy
Publication Title A long noncoding RNA regulates microtubule behaviour during mitosis
Publication Authors Stojic L, Lun ATL, Mascalchi P, Ernst C, Redmond AM, Mangei J, Cooper S, Barr AR, Taylor C, Franklin VNR, Bakal C, Marioni JC, Odom DT, Gergely F
PubMed ID 32296040 https://www.ncbi.nlm.nih.gov/pubmed/32296040
PMC ID PMC7160116 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7160116
Publication DOI 10.1038/s41467-020-14978-7 https://doi.org/10.1038/s41467-020-14978-7
Release Date 2020-03-03
License CC BY 4.0 https://creativecommons.org/licenses/by/4.0/
Copyright Stojic et al
Data Publisher University of Dundee
Data DOI 10.17867/10000133b https://doi.org/10.17867/10000133b
BioStudies Accession S-BIAD3 https://www.ebi.ac.uk/biostudies/studies/S-BIAD3
Annotation File idr0056-screenB-annotation.csv https://github.com/IDR/idr0056-stojic-lncrnas/blob/HEAD/screenB/idr0056-screenB-annotation.csv
```
Next, we can go through sub-datasets. 
We are looking at a [high content screening](https://en.wikipedia.org/wiki/High-content_screening) (HCS) data set, which typically are organized in plates. 
A [for-loop](https://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/08_loops.ipynb) allows us to take a look at available plates.

```python
PLATES_URL = "https://idr.openmicroscopy.org/webclient/api/plates/?id={screen_id}"
qs = {'screen_id': screen_id}

# assemble a specific ULR from the generic URL
url = PLATES_URL.format(**qs)

# go through all plates
for p in session.get(url).json()['plates']:
    plate_id = p['id'] # note, we will use this variable further down
    print (p['id'], p['name'], p['childCount'])
```
This will print out the identifiers of all plates related to the screen:
```
7361 1977 1
7368 1978 1
7366 1981 1
7367 1982 1
7379 1983 0
7369 1984 1
7371 1985 1
7370 1986 1
7372 1987 1
7375 1988 1
```

Plates are organized in wells (in the digital world you could call them tables) and thus, we can go through all wells
in a similar way like going through plates. 
This time, we will stop after the first row of images to just see a couple of small thumbnails of them. 
Looking at thumbnails makes a lot of sense as long as you don't need the full image data and are just browsing the database.

```python
WELLS_IMAGES_URL = "https://idr.openmicroscopy.org/webgateway/plate/{plate_id}/{field}/"
THUMBNAIL_URL = "https://idr.openmicroscopy.org/webclient/render_thumbnail/{image_id}/"

qs = {'plate_id': plate_id, 'field': 0}
url = WELLS_IMAGES_URL.format(**qs)
grid = session.get(url).json()
rowlabels = grid['rowlabels']
collabels = grid['collabels']

# go through the well of images.
for row in grid['grid']:
    for cell in row:
        if cell is not None:
            # read image specific information we will use this variable further down
            image_id = cell['id']

            # print image ID and show thumbnail
            print(image_id)
            thumbnail = imread(THUMBNAIL_URL.format(**{'image_id':image_id}))
            imshow(thumbnail)

            # leave after first image
            break

    # leave after first row
    break
```

![img_1_thumbnail.png](idr_api/img_1_thumbnail.png)

In order to retrieve the whole 2D image, we can use the code shown on top.

```python
generic_image_url = "https://idr.openmicroscopy.org/webclient/render_image/{image_id}/"

# combine generic url with image ID
image_url = generic_image_url.format(**{"image_id":image_id})

# download and show image
image = imread(image_url)
imshow(image)
```

![img_1.png](idr_api/img_1.png)

If the dataset is 3D or a timelapse (or both) downloading is a bit more complicated. 
See the [related discussion with example code on image.sc](https://forum.image.sc/t/download-3d-dataset-from-image-data-resource/53632/6).

Furthermore, we can print out the meta data using [json](https://www.json.org/json-en.html). 
Note: We can have a look at the meta data without downloading the image.

```python
import json

qs = {'image_id': image_id}
IMAGE_DETAILS_URL = "https://idr.openmicroscopy.org/webclient/imgData/{image_id}/"
url = IMAGE_DETAILS_URL.format(**qs)
r = session.get(url)
if r.status_code == 200:
    print (json.dumps(r.json(), indent=4, sort_keys=True))
```

```
{
    "channels": [
        {
            "active": true,
            "coefficient": 1.0,
            "color": "FF0000",
            "emissionWave": null,
            "family": "linear",
            "inverted": false,
            "label": "alpha-tubulin (microtubule cytoskeleton)",
            "reverseIntensity": false,
            "window": {
                "end": 187.0,
                "max": 65535.0,
                "min": 0.0,
                "start": 0.0
            }
        },
        {
            "active": true,
            "coefficient": 1.0,
            "color": "00FF00",
            "emissionWave": null,
            "family": "linear",
            "inverted": false,
            "label": "gamma-tubulin (centrosomes)",
            "reverseIntensity": false,
            "window": {
                "end": 342.0,
                "max": 65535.0,
                "min": 0.0,
                "start": 0.0
            }
        },
        {
            "active": true,
            "coefficient": 1.0,
            "color": "0000FF",
            "emissionWave": null,
            "family": "linear",
            "inverted": false,
            "label": "phospho-histone H3 serine 10 (mitotic cells)",
            "reverseIntensity": false,
            "window": {
                "end": 117.0,
                "max": 65535.0,
                "min": 0.0,
                "start": 1.0
            }
        },
        {
            "active": false,
            "coefficient": 1.0,
            "color": "FF0000",
            "emissionWave": null,
            "family": "linear",
            "inverted": false,
            "label": "Hoechst (DNA)",
            "reverseIntensity": false,
            "window": {
                "end": 381.0,
                "max": 65535.0,
                "min": 0.0,
                "start": 0.0
            }
        }
    ],
    "id": 9762957,
    "init_zoom": 0,
    "interpolate": true,
    "meta": {
        "datasetDescription": "",
        "datasetId": null,
        "datasetName": "Multiple",
        "imageAuthor": "Public data",
        "imageDescription": "",
        "imageId": 9762957,
        "imageName": "1988 [Well A-1; Field #1]",
        "imageTimestamp": 1404512029.0,
        "pixelsType": "uint16",
        "projectDescription": "",
        "projectId": null,
        "projectName": "Multiple",
        "wellId": 1475376,
        "wellSampleId": ""
    },
    "perms": {
        "canAnnotate": false,
        "canDelete": false,
        "canEdit": false,
        "canLink": false
    },
    "pixel_range": [
        0,
        65535
    ],
    "pixel_size": {
        "x": 0.6459,
        "y": 0.6459,
        "z": null
    },
    "rdefs": {
        "defaultT": 0,
        "defaultZ": 0,
        "invertAxis": false,
        "model": "color",
        "projection": "normal"
    },
    "size": {
        "c": 4,
        "height": 493,
        "t": 1,
        "width": 659,
        "z": 1
    },
    "split_channel": {
        "c": {
            "border": 2,
            "gridx": 3,
            "gridy": 2,
            "height": 992,
            "width": 1985
        },
        "g": {
            "border": 2,
            "gridx": 2,
            "gridy": 2,
            "height": 992,
            "width": 1324
        }
    },
    "tiles": false
}
```
