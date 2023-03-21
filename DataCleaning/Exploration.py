import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

SourceDir = 'C:/Users/PC/Desktop/Master Thesis/Data/PickleData/OpenPowerSystemData/'
FileName = 'time_series_60min_singleindex_filtered_DK1'
df = pd.read_pickle(SourceDir + FileName + '.pkl')