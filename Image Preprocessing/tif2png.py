from libtiff import TIFF
import sys
import numpy as np
import os
from PIL import Image
from os import listdir
from os.path import isfile, join
import pickle
import h5py
import scipy.misc
import glob
import numpy as np
import gdalnumeric


# statelist = {'UP','UK','TR','TN','SK','RJ','PB','OR','MZ','MP',
# 'MN','MH','KL','KA','JH',
# 'HR','GJ','CG','BR','AS','AP'}
#statelist = {'UK','RJ','OR','MZ','MP'}
statelist = ['UP','TR']
for state in statelist:

	folder_containing_tifffiles = 'state_cutFiles' + '/' + state + '_cutFiles'
	inputFolder = folder_containing_tifffiles

	outputFolder = 'state_png/' + state +'_png'

	if not os.path.exists(outputFolder):
	    os.makedirs(outputFolder)

	onlyfiles = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]


	for currImageName in onlyfiles:
		# currImageName='Landsat7_MedianAndhraPradesh_2011-0000000000-0000000000@80200@569751.tif'
		destImageName=currImageName
		tif = TIFF.open(inputFolder+'/'+currImageName, mode='r')
		image = tif.read_image()
		data = np.array(image)
		print(currImageName)
		print(image.shape)
		size = image.shape
		if size[0]>30 and size[1]>30 :		
			## Concat the images
			scipy.misc.imsave(outputFolder+'/'+destImageName[:-4]+'.png', np.stack([data[:,:,0],data[:,:,1],data[:,:,2]],axis = 2))
			#scipy.misc.imsave(outputFolder+'/'+destImageName[:-4]+'.png', np.stack([data[:,0]],axis = 1))





