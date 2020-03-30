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

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

for state in statelist:
	print(state)
	folder_containing_tifffiles = 'state_png' + '/' + state + '_png'
	inputFolder = folder_containing_tifffiles

	outputFolder = 'state_150x/' + state +'_150x' 

	if not os.path.exists(outputFolder):
	    os.makedirs(outputFolder)

	onlyfiles = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]


	for currImageName in onlyfiles:
		# currImageName='Landsat7_MedianAndhraPradesh_2011-0000000000-0000000000@80200@569751.png'
		path_currImageName = folder_containing_tifffiles + '/' + currImageName
		out_image = currImageName
		path_out_image = outputFolder + '/' + out_image
		im = Image.open(path_currImageName)
		im_new = crop_center(im, 150, 150)
		im_new.save(path_out_image, quality=100)





