#
# Taken from :
#  turing-project, Nils Hamel
#  Copyright (C) 2016-2018 DHLAB, EPFL
#  GNU General Public License v 3.0
#  https://github.com/nils-hamel/turing-project.git
#

# Imports
import sys
import numpy as np

def ml_raster_convert( ml_raster ):
    ''' Convert rasters in form of a serie of 0 and 1 (1 = point) into an array containing the
        coordinates of the points '''
    """
        Args:
            ml_raster(numpy 3 dim array): the array containing a serie of 0 and 1
    """

    # check consistency #
    if ( ( ml_raster.shape[0] != ml_raster.shape[1] ) or ( ml_raster.shape[0] != ml_raster.shape[2] ) ):

        # send message #
        sys.exit( 'turing : error : raster not consistent' )

    # retrieve raster width #
    ml_width = ml_raster.shape[0]

    # initialise array #
    ml_data = np.empty( ( 0, 3 ), dtype=np.uint8 )

    # parsing raster array #
    for ml_x in range( ml_width ):

        # parsing raster array #
        for ml_y in range( ml_width ):

            # parsing raster array #
            for ml_z in range( ml_width ):

                # check raster element #
                if ( ml_raster[ml_x, ml_y, ml_z] != 0 ):

                    # compute element coordinates #
                    ml_r = ml_x / ml_width
                    ml_s = ml_y / ml_width
                    ml_t = ml_z / ml_width

                    # append element #
                    ml_data = np.append( ml_data, np.array( [[ ml_r, ml_s, ml_t ]] ), axis=0 )

    # return converted array #
    return( ml_data )
