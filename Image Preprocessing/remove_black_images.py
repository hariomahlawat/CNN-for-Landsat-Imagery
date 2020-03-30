import sys
import numpy as np
import os
import PIL
from PIL import Image
from os import listdir
from os.path import isfile, join
import scipy.misc
import glob
import numpy as np
import gdalnumeric


statelist = {'UP','UK','TR','TN','SK','RJ','PB','OR','MZ','MP',
'MN','MH','KL','KA','JH',
'HR','GJ','CG','BR','AS','AP'}


for state in statelist:
	print(state)
	folder_containing_tifffiles = 'state_150x' + '/' + state + '_150x'
	inputFolder = folder_containing_tifffiles

	onlyfiles = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]

	for currImageName in onlyfiles:
		# currImageName='Landsat7_MedianAndhraPradesh_2011-0000000000-0000000000@80200@569751.png'
		path_currImageName = folder_containing_tifffiles + '/' + currImageName
		img = Image.open(path_currImageName)
		if not img.getbbox():
			print(currImageName)
			os.remove(path_currImageName)
			





