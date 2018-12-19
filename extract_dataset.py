# Taken from :
#   turing-project Copyright (C) 2017 Nils Hamel
#
# GNU General Public License v 3.0
# https://github.com/nils-hamel/turing-project.git
#

# Import
import numpy
import os
import sys
import random
import ml_args

##
##  script - raster exportation
##

def ml_raster_export( ml_data, ml_path ):

    # create output stream #
    with open( ml_path, 'ab' ) as ml_file:

        # export raster array #
        numpy.array( ml_data, dtype=numpy.uint8 ).tofile( ml_file )

##
##  script - dataset importation
##

def ml_raster_import( ml_path, ml_width ):

    # check consistency #
    if ( not os.path.exists( ml_path ) ):

        # send message #
        sys.exit( 'turing : error : unable to access dataset' )

    # create input stream #
    with open( ml_path, 'rb' ) as ml_file:

        # import bytes #
        ml_byte = ml_file.read( os.path.getsize( ml_path ) )

    # convert to numpy array #
    ml_data = numpy.frombuffer( ml_byte, dtype=numpy.uint8 )

    # return dataset #
    return( ml_data.reshape( -1, ml_width, ml_width, ml_width ) )

##
##  script - dataset import
##

def ml_dataset_import( ml_args_dataset, ml_args_raster, ml_args_width ):
    
    # import dataset #
    ml_data = ml_raster_import( ml_args_dataset, ml_args_width )

    # check script mode #
    if ( ml_args.mode == 'full' ):

        # parsing dataset #
        for ml_parse in range( ml_data.shape[0] ):

            # export raster #
            ml_raster_export( ml_data[ml_parse], ml_args_raster + '/raster-{:06d}.ras'.format( ml_parse ) )

        # display information #
        print( 'turing : done' )

    elif ( ml_args.mode == 'sample' ):

        # parsing dataset #
        for ml_parse in range( ml_args.count ):

            # create random index #
            ml_index = random.randint( 0, ml_data.shape[0] - 1 )

            # export raster #
            ml_raster_export( ml_data[ml_index], ml_args_raster + '/raster-{:06d}.ras'.format( ml_index ) )
            
    return 'Task completed'

