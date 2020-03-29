# CNN-for-Landsat-Imagery
This includes scripts for downloading Landsat images from GEE, cutting of imagery using shapefiles (Indian Villages), converting .tiff images to .png, cropping images from center and CNN model scripts.   

## Image Preprocessing
* **1. Download Landsat Imagery** - we have downloaded Landsat7 imagery for the year 2011.  
* **2. Cut Images using village shapefiles**
* **3. Convert images from .tif to .png**
* **4. Remove noisy Images** - There were few black images (completelly black) present in each state. We removed those black images.
* **5. Crop images from centre** - we cropped each vilaages image (150 x 150 pixels) from centre.

Scripts for all the aboves steps are present in this repo.
