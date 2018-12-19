#   3D_pointclouds_super-resolution Copyright (C) 2018
#   Rémi Petitpierre, Anna Fredriksson Häägg, Martin Sigmund
#
# GNU General Public License v 3.0
# https://github.com/RPetitpierre/3D_pointclouds_super-resolution
#

def init() :
    
    # Initialize global variables
    global mode
    global dataset_low_res
    global dataset_high_res
    global width_low_res
    global width_high_res

    global raster_low_res
    global raster_high_res
    global count

    global model


    # Extract dataset variables
    mode = 'full'
    dataset_low_res = './data/16x16x16-geneva-2005'
    dataset_high_res = './data/32x32x32-geneva-2005'
    width_low_res = 16
    width_high_res = 32

    # Shared variables
    raster_low_res = './raster/low_res'
    raster_high_res = './raster/high_res'
    count = '13597'
    
    # Reload data variable  
    model = './model/'

return True