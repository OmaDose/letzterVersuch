#!/bin/python
# -*- coding: iso-8859-15 -*-
#Author: Johanna Schwehn 2015
#Assignment 2
#Generate a 3D Point Cloud of the Cell Centers of a DEM
#python rast2cloud.py dsm.tif output_ascii.xyz min_elevation max_elevation
###########################################

'''
Jakob war hier
'''

#required modules
import sys
from numpy import *
from osgeo import gdal

#enable error-reports by rising exceptions fpr GDAL
gdal.UseExceptions()

#arguments provided as user input
try:
	infile = sys.argv[1] #dsm.tif
	#outfile = sys.argv[2] #output_ascii.xyz
	#min_elevation  = sys.argv[3] #min_elevation
	#max_elevation = sys.argv[4] #max_elevation
except:
	print "rast2cloud.py dsm.tif output_ascii.xyz min_elevation max_elevation"
	sys.exit(1)

#open input raster file
ds = gdal.Open(infile)
if ds is None:
	print "Could not open %s" % (infile)
	sys.exit(1)

#access single pixel/cells
cols = ds.RasterXSize
rows = ds.RasterYSize
bands = ds.RasterCount

band = ds.GetRasterBand(1)
data = band.ReadAsArray(0, 0, cols, rows)

print data

#delete data from memory
data = None
ds = None
band = None
