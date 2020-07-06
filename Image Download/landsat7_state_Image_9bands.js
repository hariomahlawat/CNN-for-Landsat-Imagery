/**
 * Function to mask clouds based on the pixel_qa band of Landsat SR data.
 * @param {ee.Image} image Input Landsat SR image
 * @return {ee.Image} Cloudmasked Landsat image
 */
var cloudMaskL457 = function(image) {
  var qa = image.select('pixel_qa');
  // If the cloud bit (5) is set and the cloud confidence (7) is high
  // or the cloud shadow bit is set (3), then it's a bad pixel.
  var cloud = qa.bitwiseAnd(1 << 5)
                  .and(qa.bitwiseAnd(1 << 7))
                  .or(qa.bitwiseAnd(1 << 3));
  // Remove edge pixels that don't occur in all bands
  var mask2 = image.mask().reduce(ee.Reducer.min());
  return image.updateMask(cloud.not()).updateMask(mask2);
};



var year_list = ['2011'];


var state_list =['Madhya Pradesh','Maharashtra','Haryana','Punjab','Karnataka','Jharkhand','Andhra Pradesh','Telangana','Chhattisgarh','Uttar Pradesh'];

//var state_list = ['Uttarakhand','Tripura','Tamil Nadu','Sikkim','Kerala','Gujarat','Bihar','Odisha','Rajasthan','Manipur','Mizoram','Assam']


// var bands = ['B3', 'B2', 'B1'];
var bands = ['B1','B2', 'B3', 'B4', 'B5', 'B6','B7'];
var india = ee.FeatureCollection('users/hariomahlawat/India_Boundary')
    .geometry();

function add_all_bands(median_image, min_image, max_image){
  return median_image.select('B1','B2','B3')
  .addBands(min_image.select('B1','B2','B3'))
  .addBands(max_image.select('B1','B2','B3'));
  
}

for (var i in state_list) {
  
  var state_name = state_list[i];
  
  var state = ee.FeatureCollection('users/hariomahlawat/India_States')
    .filter(ee.Filter.eq('ST_NM',state_name));
    
    
  for (var j in year_list)
  {
     var year = year_list[j];
     var str = state_name.replace(/\s/g,'');
   
    var state_image = ee.ImageCollection('LANDSAT/LE07/C01/T1_SR')
    .filterBounds(india)
    .filterDate('2011-01-01','2011-03-31')
    .filter(ee.Filter.lt('CLOUD_COVER',5))
    .sort('CLOUD_COVER')
    // .limit(500)
    .map(cloudMaskL457)
    .select(bands)
    ;

    
    var state_image_min = state_image.select(bands).min();
    var state_image_max = state_image.select(bands).max();
    var state_image_median = state_image.select(bands).median();
    var state_image = add_all_bands(state_image_median,
                                state_image_min,
                                state_image_max);
    state_image = state_image.toFloat()                            
    print(state_image)     
   
   
   
     
      Export.image.toDrive({
        image: state_image.clip(state),
        description: 'Landsat7_MinMaxMedian_'+str + '_' + year,
        maxPixels: 499295920080,
        scale: 30,
        folder: 'LandSat7_2011__MinMaxMedian_RGB',
        region: state.geometry().bounds()
      });
  }
 
}