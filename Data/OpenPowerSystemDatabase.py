import pandas as pd
import datetime as dt

SourceDir = 'C:/Users/PC/Desktop/Master Thesis/Data/RawData/OpenPowerSystemData/'
FileName = 'time_series_60min_singleindex_filtered_DK1'
SaveDir = 'C:/Users/PC/Desktop/Master Thesis/Data/PickleData/OpenPowerSystemData/'


df = pd.read_csv(SourceDir + FileName + '.csv')
df = df.drop(columns='utc_timestamp')
df = df.rename(columns={'cet_cest_timestamp': 'timestamp'})

df.to_pickle(SaveDir + FileName + '.pkl')