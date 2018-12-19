3D_pointclouds_super-resolution. Copyright (C) 2018

Rémi Petitpierre, Anna Fredriksson Häägg, Martin Sigmund. Ecole polytechnique fédérale de Lausanne – EPFL

GNU General Public License v 3.0. https://github.com/RPetitpierre/3D_pointclouds_super-resolution

# Files and folders description

### main.ipynb ###

Jupyter notebook which will run the whole model by calling the various different functions. This notebook also directly contains all the machine learning part of the project, including the neural network as well as the training and testing algorithms, that we implemented

### extract_dataset.py ###

The functions contained in this python file help to cut the massive dataset in individual raster files (.ras format, composed of zeros and ones). They were directly furnished by the hosting lab (see reference below).

Taken from :
 turing-project, Nils Hamel
 Copyright (C) 2016-2018 DHLAB, EPFL
 GNU General Public License v 3.0
 https://github.com/nils-hamel/turing-project.git


### raster_convert.py ###

The ml_raster_convert function it contains helps to convert rasters (composed of zeros and ones) into points coordinates contained in a 3D numpy array. This function was directly furnished by the hosting lab (see reference below).

Taken from :
 turing-project, Nils Hamel
 Copyright (C) 2016-2018 DHLAB, EPFL
 GNU General Public License v 3.0
 https://github.com/nils-hamel/turing-project.git


### output_display.py ###

Contains various functions used for post-processing and displaying outputs.

Parts of the code is adapted from :
 turing-project, Nils Hamel
 Copyright (C) 2016-2018 DHLAB, EPFL
 GNU General Public License v 3.0
 https://github.com/nils-hamel/turing-project.git


### ml_args.py ###

This python file contains the arguments (global variables) that are used by the other functions dealing with the raster files.


### data ###

This folder is the supposed location of the full dataset.


### model ###

This folder contains the model file which is created during the training process.


### raster ###

This folder is subdivided between the high_res and low_res folders which are meant to contain the individual rasters once they have been extracted (see extract_dataset.py).

# Dataset Description

For this project 3D LIDAR data of the city of Geneva in the year 2005 was used. The dataset belongs to the EPFL DHLAB, this is the reason why it is not furnished there. It is composed of 13597 rasters  (volumetric  elements), each encoding one  part of the Geneva region. For each raster there are both a high- and low-resolution version. 32x32x32 binary pixels (high resolution) and 16x16x16 binary pixels (low  resolution). Each raster covers roughly 153 m in width, length and height with a precision of roughly 4,8 m for the high resolution data and 9,6 m for the low-resolution data. Additional informations, including on the rest of the dataset (which was not used in this project) can be found at the following address : https://github.com/nils-hamel/turing-project/blob/master/README.md

# Library dependencies

Python core libraries :
* random
* os
* sys

External libraries :
* torch : Deep convolutional neural network implementation and evaluation
* sklearn : Splitting test and train set
* numpy : 3D data handling and regular computation
* matplotlib : Visualization of 3D data
* IPython.display : Image display in the Jupyter notebook



