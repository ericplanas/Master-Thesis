#import requests
#import geopandas as gpd

#url = "https://gisco-services.ec.europa.eu/grid/grid_1km_point.gpkg"

#response = requests.get(url)

#data = response.content

#grid = gpd.read_file(data, driver='GPKG')

#print(grid.head())

import geopandas as gpd
SourceDir = 'C:/Users/PC/Desktop/Master Thesis/Data/Railway network/'
FileName = 'Railway.geojson'

mydata = gpd.read_file(SourceDir + FileName)
print('a')