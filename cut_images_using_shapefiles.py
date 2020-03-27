import json
import sys
import rasterio
from rasterio.mask import mask
from json import loads
import sys
import os
from os import listdir
from os.path import isfile, join

statelist = {'UP','UK','TR','TN','SK','RJ','PB','OR','MZ','MP',
'MN','MH','KL','KA','JH',
'HR','GJ','CG','BR','AS','AP'}



for state in statelist:

    folder_containing_tifffiles = 'state_tiff' + '/' + state
    json_file = 'state_json' + '/' + state + '.geojson' 
    output_directory = state +'_cutFiles'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    allTiffFiles = [f for f in listdir(folder_containing_tifffiles) if isfile(join(folder_containing_tifffiles, f))]
    jsonFileList = [json_file]

    for tiffFileName in allTiffFiles:
        for jsonFileName in jsonFileList:
            stateData = json.loads(open(jsonFileName).read())
            print('tiffFileName',tiffFileName)
            print('jsonFileName',jsonFileName)
            for currVillageFeature in stateData["features"]:
                try:
                    vCode2001=currVillageFeature["properties"]["pc01_village_id"]
                    vCode2011=currVillageFeature["properties"]["pc11_village_id"]
                    geoms=currVillageFeature["geometry"]
                    listGeom=[]
                    listGeom.append(geoms)
                    geoms=listGeom
                    with rasterio.open(folder_containing_tifffiles+'/'+tiffFileName) as src:
                        out_image, out_transform = mask(src, geoms, crop=True)

                    out_meta = src.meta.copy()
                    # save the resulting raster  
                    out_meta.update({"driver": "GTiff",
                        "height": out_image.shape[1],
                        "width": out_image.shape[2],
                    "transform": out_transform})
                    saveFileName= output_directory+'/'+tiffFileName[:-4]+"@"+str(vCode2001)+"@"+str(vCode2011)+".tif"
                    with rasterio.open(saveFileName, "w", **out_meta) as dest:
                        dest.write(out_image)
                except:
                    continue