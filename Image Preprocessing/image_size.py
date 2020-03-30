import json
import sys
import rasterio
from rasterio.mask import mask
from json import loads
import sys
import os
from os import listdir
from os.path import isfile, join
import pickle

statelist = {'UP','UK','TR','TN','SK','RJ','PB','OR','MZ','MP',
'MN','MH','KL','KA','JH',
'HR','GJ','CG','BR','AS','AP'}



final_list_images_size = []
for state in statelist:
    print(state)
    folder_containing_tifffiles = 'state_cutFiles' + '/' + state + '_cutFiles' 

    allTiffFiles = [f for f in listdir(folder_containing_tifffiles) if isfile(join(folder_containing_tifffiles, f))]
    temp_list = []
    for tiffFileName in allTiffFiles:
        #print('tiffFileName',tiffFileName)
        img = rasterio.open(folder_containing_tifffiles + '/' + tiffFileName)
        img = img.read(1)
        vill_code = tiffFileName.split('@')
        vcode_2001 = vill_code[1]
        vcode_2011 = vill_code[2].split('.')[0]
        #print('Village Code 2001', vcode_2001)
        #print('Village Code 2011', vcode_2011)
        image_size = img.shape
        #print(image_size)
        temp_list = [state,vcode_2001,vcode_2011]
        #print(temp_list)
        final_list_images_size.append(temp_list)
#print(final_list_images_size)
with open('clean_list_images.pkl', 'wb') as f:
    pickle.dump(final_list_images_size, f)


