# Image Preprocessing
* **1. Download Landsat Imagery** - we have downloaded Landsat7 imagery for the year 2011.  
* **2. Cut Images using village shapefiles**
* **3. Convert images from .tif to .png**
* **4. Remove noisy Images** - There were few black images (completelly black) present in each state. We removed those black images.
* **5. Crop images** - we cropped each vilaages image (150 x 150 pixels) from centre.

Scripts for all the aboves steps are present in this folder.

* **Image Size Analysis** - image_size.py stores the state, village code 2001, village code 2011 and image size for each village in a list ans saves it in pickle file. analysis_image_size.ipynb is for analysis of image size.
