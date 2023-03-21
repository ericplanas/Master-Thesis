import pandas as pd
import geopandas as gpd

SourceDir = 'C:/Users/PC/Desktop/Master Thesis/Data/RawData/Railway network/'
SaveDir = 'C:/Users/PC/Desktop/Master Thesis/Data/PickleData/Railway network/'
columns = ['railway', 'geometry']

df = gpd.read_file(SourceDir + 'Railway.geojson')

df = df[(df.railway == 'rail') | (df.railway == 'subway') | (df.railway == 'light_rail')]
df = df[columns]

df.to_pickle(SaveDir + 'Railway.pkl')