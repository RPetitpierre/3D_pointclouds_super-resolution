
   3D_pointclouds_super-resolution
   
   Copyright (C) 2018
   
   Rémi Petitpierre, Anna Fredriksson Häägg, Martin Sigmund
   
   Ecole polytechnique fédérale de Lausanne – EPFL
   

   GNU General Public License v 3.0
   
   https://github.com/RPetitpierre/3D_pointclouds_super-resolution


# Files and folders description


### run.ipynb

Jupyter notebook which will run the whole model by calling the various different functions. This notebook also directly contains all the machine learning part of the project, including the neural network as well as the training and testing algorithms, that we implemented


### extract_dataset.py

The functions contained in this python file help to cut the massive dataset in individual raster files (.ras format, composed of zeros and ones). They were directly furnished by the hosting lab (see reference below).

Functions :
* ml_raster_export(ml_data, ml_path)
* ml_raster_import(ml_path, ml_width)
* ml_dataset_import(ml_args_dataset, ml_args_raster, ml_args_width)
 

Taken from :
 turing-project, Nils Hamel
 Copyright (C) 2016-2018 DHLAB, EPFL
 GNU General Public License v 3.0
 https://github.com/nils-hamel/turing-project.git


### load_data.py

These functions will help to import rasters contained in .ras files and load them in the form of numpy arrays. They were directly furnished by the hosting lab (see reference below).

Functions :
* ml_raster_import(ml_path)
* get_ml_data(ml_args_raster)

Adapted from :
 turing-project, Nils Hamel
 Copyright (C) 2016-2018 DHLAB, EPFL
 GNU General Public License v 3.0
 https://github.com/nils-hamel/turing-project.git


### raster_convert.py

The function it contains helps to convert rasters (composed of zeros and ones) into points coordinates contained in a 3D numpy array. This function was directly furnished by the hosting lab (see reference below).

Functions :
* ml_raster_convert(ml_raster)

Taken from :
 turing-project, Nils Hamel
 Copyright (C) 2016-2018 DHLAB, EPFL
 GNU General Public License v 3.0
 https://github.com/nils-hamel/turing-project.git


### output_display.py

Contains various functions used for post-processing and displaying outputs.

Functions:
* find_ground(flatten, position, size)
* flatten_ground(size, raster)
* complete_ground(raster)
* print_3D(y, n, m, mode)
* print_3D_pred(y, x, n = 0, advanced_mode = True)


### ml_args.py

This python file contains the arguments (global variables) that are used by the other functions dealing with the raster files.

Functions :
 init()


### __pycache__

Will automatically be created by Python when running the code.


### data

This folder is the supposed location of the full dataset.


### model

This folder contains the model file which is created during the training process.


### raster

This folder is subdivided between the high_res and low_res folders which are meant to contain the individual rasters once they have been extracted (see extract_dataset.py).


### img

Just contains the beautiful cnn_model image displayed in the Jupyter notebook.


# Dataset Description

For this project 3D LIDAR data of the city of Geneva in the year 2005 was used. The dataset belongs to the EPFL DHLAB, this is the reason why it is not furnished there. It is composed of 13597 rasters  (volumetric  elements), each encoding one  part of the Geneva region. For each raster there are both a high- and low-resolution version. 32x32x32 binary pixels (high resolution) and 16x16x16 binary pixels (low  resolution). Each raster covers roughly 153 m in width, length and height with a precision of roughly 4,8 m for the high resolution data and 9,6 m for the low-resolution data. Additional informations, including on the rest of the dataset (which was not used in this project) can be found at the following address : https://github.com/nils-hamel/turing-project/blob/master/README.md


# Library dependencies

In order to run the program, you will need to have the following libraries installed :

Python core libraries :
* random
* os
* sys

External libraries :
* torch
     "Pytorch"
     Deep convolutional neural network implementation and evaluation
     https://pytorch.org/docs/stable/index.html

* sklearn
     "Scikit learn"
     Splitting test and train set
     https://scikit-learn.org/stable/documentation.html
     
* numpy
     3D data handling and regular computation
     https://docs.scipy.org/doc/

* matplotlib
     Visualization of 3D data
     https://matplotlib.org/contents.html

* IPython.display
     Image display in the Jupyter notebook
     https://ipython.org/ipython-doc/3/api/generated/IPython.display.html


# OS Requirements

The project runs on Mac OSX. Please consider that the pytorch library is still unstable on Windows and the code may therefore not run on certain PCs.
