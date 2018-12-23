#   3D_pointclouds_super-resolution Copyright (C) 2018
#   Rémi Petitpierre, Anna Fredriksson Häägg, Martin Sigmund
#
# GNU General Public License v 3.0
# https://github.com/RPetitpierre/3D_pointclouds_super-resolution
#

# Imports
import numpy as np
import ml_args

# Matplotlib to visualize the result
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
import matplotlib.cm as cm


def find_ground(flatten, position, size):
    ''' Find the ground level from the direct neighbours of the position '''
    """
        Args:
          flatten(2 dims numpy array): Square flatten representation of the ground
          position(tuple(int,int)): Position in the 2d flatten array
          size(int): Edge length of the 2d flatten array
    """
    
    ground = 0
    neighbours = []
    
    if position[0] == 0:
        if position[1] == 0:
            neighbours = ([flatten[position[1]+1][position[0]],
                           flatten[position[1]][position[0]+1],
                           flatten[position[1]+1][position[0]+1]])
        elif position[1] == size-1:
            neighbours = ([flatten[position[1]-1][position[0]],
                           flatten[position[1]][position[0]+1],
                           flatten[position[1]-1][position[0]+1]])
        else:
            neighbours = ([flatten[position[1]+1][position[0]],
                           flatten[position[1]-1][position[0]],
                           flatten[position[1]][position[0]+1],
                           flatten[position[1]+1][position[0]+1],
                           flatten[position[1]-1][position[0]+1],
                           flatten[position[1]][position[0]+2]])
                
    elif position[0] == size-1:
        if position[1] == 0:
            neighbours = ([flatten[position[1]+1][position[0]],
                           flatten[position[1]][position[0]-1],
                           flatten[position[1]+1][position[0]-1]])
        elif position[1] == size-1:
            neighbours = ([flatten[position[1]-1][position[0]],
                           flatten[position[1]][position[0]-1],
                           flatten[position[1]-1][position[0]-1]])
        else:
            neighbours = ([flatten[position[1]+1][position[0]],
                           flatten[position[1]-1][position[0]],
                           flatten[position[1]][position[0]-1],
                           flatten[position[1]+1][position[0]-1],
                           flatten[position[1]-1][position[0]-1],
                           flatten[position[1]][position[0]-2]])
                
    elif position[1] == 0:
        neighbours = ([flatten[position[1]+1][position[0]],
                       flatten[position[1]+1][position[0]+1],
                       flatten[position[1]+1][position[0]-1],
                       flatten[position[1]][position[0]+1],
                       flatten[position[1]][position[0]-1],
                       flatten[position[1]+2][position[0]]])
                
    elif position[1] == size-1:
        neighbours = ([flatten[position[1]-1][position[0]],
                       flatten[position[1]-1][position[0]+1],
                       flatten[position[1]-1][position[0]-1],
                       flatten[position[1]][position[0]+1],
                       flatten[position[1]][position[0]-1],
                       flatten[position[1]-2][position[0]]])
                
    else:
        neighbours = [flatten[position[1]+1][position[0]], flatten[position[1]-1][position[0]],
                      flatten[position[1]][position[0]+1], flatten[position[1]+1][position[0]-1],
                      flatten[position[1]+1][position[0]+1], flatten[position[1]-1][position[0]+1],
                      flatten[position[1]+1][position[0]-1], flatten[position[1]-1][position[0]-1]]
    
    if (np.count_nonzero(neighbours)) != 0:
        ground = np.around(np.sum(neighbours)/np.count_nonzero(neighbours))
    
    return ground


def flatten_ground(size, raster):
    ''' Establish a 2D array containing the ground level, like a topological map '''
    """
        Args:
          size(int): Edge length of the 3d raster
          aster(3 dims numpy array): 3D representation of the LIDAR cloudpoints
    """

    flatten = np.zeros((size, size))
    
    # Establish a 2D array containing the ground level
    for i in range(size) :
        for j in range(size):
            
            arg_max = raster.swapaxes(2, 0)[j][i].argmax()
            
            if (arg_max == 0):
                if (raster.swapaxes(2,0)[j][i][0] != 0):
                    flatten[j][i] = 1
                else :
                    flatten[j][i] = 0
            else :
                flatten[j][i] = arg_max + 1 
    
    return flatten


def complete_ground(raster):
    ''' For each vertical column of the raster, verify if it is empty.
        In the case it is, fill it with the nearest neighbour value. '''
    
    size = len(raster[0][0])
    flatten = flatten_ground(size, raster)
        
    # Complete the missing ground levels
    completed = np.copy(flatten)
    half = int(np.floor(size/2))
    for a in range(half):
        for i in range(0+half-a, size-half+a):
            for j in range(0+half-a, size-half+a):
                if completed[j][i] == 0:
                    completed[j][i] = find_ground(completed, (j, i), size)
                    
    while np.min(completed) == 0 :
        for i in range(0, size):
            for j in range(0, size):
                if completed[j][i] == 0:
                    completed[j][i] = find_ground(completed, (j, i), size)
                    
                        
    # Add all ground points
    for i in range(size):
        for j in range(size):
            if flatten[i][j] == 0:
                raster[int(completed[j][i])-1][j][i] = 1.
                
    return raster


def print_3D(y, n, m, mode):
    ''' Print 3D visualization of the raster n '''
    """
        Args:
            y(3 dims numpy array): pointcloud as serie of 1 and 0
            n(int): indice of the batch you want to visualize
            m(int): indice of the raster you want to visualize
            mode(string):  'x' if you want to visualize the inputs
                           'y' if you want to visualize the labels
    """
    
    if mode == 'x':
        Y = y[n][m][0].detach().numpy()
    else:
        Y = y[n][m].detach().numpy()
        
    Y = ml_raster_convert(Y)
    
    # create figure #
    ml_figure = plt.figure()

    # create figure sub-plot #
    ml_plot = ml_figure.add_subplot(111, projection='3d' )

    ml_plot.scatter(Y[:,2], Y[:,1], Y[:,0], s=8, marker='.')
    # setting axis aspect ratio #
    ml_plot.set_aspect( 'equal' )

    # setting axis limits #
    ml_plot.set_xlim( 0.0, 1.0 )
    ml_plot.set_ylim( 0.0, 1.0 )
    ml_plot.set_zlim( 0.0, 1.0 )

    # setting plot initial camera view #
    ml_plot.view_init( elev=66, azim=225 )
        
    return True


def print_3D_pred(y, x, n, m = 0, advanced_mode = True):
    ''' Print 3D visualization of the prediction raster n '''
    """
        Args:
            y(4 dims numpy array): SR pointcloud as serie of 1 and 0
            x(5 dims numpy array): LR pointcloud as serie of 1 and 0
            n(int): indice of the raster you want to visualize
            advanced_mode(bool): enable/disable the dilatation algorithm
    """
    
    Y = y[n][m].detach().numpy()

    Y = np.copy(y[n][m].detach().numpy())
    
    Y = y[n][m].detach().numpy()
    print(np.min(Y), np.mean(Y), np.median(Y), np.max(Y), np.percentile(Y, 99))
        
    Y[Y <= 0.5] = 0.
    Y[Y > 0.5] = 1.
    
    raster = np.copy(Y)
    
    # dilatation algorithm
    if advanced_mode:
        mode = 'vanilla'
    
        X = x[n][m][0].detach().numpy()
    
        flatten = flatten_ground(len(X[0]), X)
    
        # If the ground is naturally containing gaps, we don't complete the ground ('vanilla' mode)
        # In the contrary, if the input's ground is continuous, the output's ground should also be continuous
        
        if np.min(flatten) == 0:
            mode = 'vanilla'
        elif np.max(flatten) == 0:
            mode = 'vanilla'
        else:
            mode = 'chocolate'
        
        if mode != 'vanilla':
            raster = complete_ground(raster)
            raster = ml_raster_convert(raster)
        else:
            raster = ml_raster_convert(Y)
    else:
        raster = ml_raster_convert(Y)
        
    # create figure #
    ml_figure = plt.figure()

    # create figure sub-plot #
    ml_plot = ml_figure.add_subplot(111, projection='3d' )

    ml_plot.scatter(raster[:,2], raster[:,1], raster[:,0], s=8, marker='.')
    # setting axis aspect ratio #
    ml_plot.set_aspect( 'equal' )

    # setting axis limits #
    ml_plot.set_xlim( 0.0, 1.0 )
    ml_plot.set_ylim( 0.0, 1.0 )
    ml_plot.set_zlim( 0.0, 1.0 )

    # setting plot initial camera view #
    ml_plot.view_init( elev=66, azim=225 )
        
    return True
