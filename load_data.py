#
# Adapted from :
#  turing-project, Nils Hamel
#  Copyright (C) 2016-2018 DHLAB, EPFL
#  GNU General Public License v 3.0
#  https://github.com/nils-hamel/turing-project.git
#

# Imports
import numpy as np
import os
import ml_args


def ml_raster_import( ml_path ):
    ''' Import a raster found at given the path '''
    """
        Args:
            ml_path(string): the full path of the raster .ras to import
    """

    # check consistency #
    if ( not os.path.exists( ml_path ) ):

        # send message #
        sys.exit( 'turing : error : unable to access raster' )

    # retrieve raster size #
    ml_size = os.path.getsize( ml_path )

    # compute raster width #
    ml_width = int( round( ml_size ** ( 1.0 / 3.0 ) ) )

    # import raster data #
    with open( ml_path, 'rb' ) as ml_file:

        # read raster bytes #
        ml_byte = ml_file.read( ml_size )

    # convert to numpy array #
    ml_data = np.frombuffer( ml_byte, dtype=np.uint8 )

    # return raster array #
    return ml_data.reshape( ml_width, ml_width, ml_width )


def get_ml_data(ml_args_raster):
    ''' Calls ml_raster_import to import all rasters '''
    """
        Args:
            ml_args_raster(string): the rasters folder path
    """

    ml_data = []
    
    for raster_id in range(0, int(ml_args.count)):
        
        raster_path = ml_args_raster + '/raster-{:06d}.ras'.format(raster_id)
    
        # import raster array #
        data = ml_raster_import(raster_path)
    
        ml_data.append(data)
        
    return ml_data

