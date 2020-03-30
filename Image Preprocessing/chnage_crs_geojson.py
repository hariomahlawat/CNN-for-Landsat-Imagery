import geopandas as gpd

# statelist = ['UK','TN','SK','RJ','PB','OR','MZ','MP','MN','MH','KL','KA','JH',
# 'HR','GJ','CG','BR','AS','AP']
statelist = ['UP','TR']


for state in statelist:
  print(state)
  df = gpd.read_file('state_json'+'/'+state+ '.geojson')
  df = df.to_crs('EPSG:4326')
  df.to_file(state+'.geojson', driver='GeoJSON')