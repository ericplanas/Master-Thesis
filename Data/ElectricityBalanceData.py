import pandas as pd
import matplotlib.pyplot as plt

# Data from ENERGINET, EnergyBalanceNonValidated dataset
# This algorithm reads the json downloaded from the website with any query, puts all the data in a suitable format and
# saves the pickle in the PickleData folder



SourceDir = 'C:/Users/PC/Desktop/Master Thesis/Data/RawData/TimeSeries/'
SaveDir = 'C:/Users/PC/Desktop/Master Thesis/Data/PickleData/TimeSeries/'
FileName = 'ElectricityBalanceNonv'

df = pd.read_json(SourceDir + FileName + '.json')
df.HourDK = pd.to_datetime(df.HourDK, format = '%Y-%m-%dT%H:%M:%S')
df = df.drop(columns=['HourUTC','PriceArea'])
df = df.set_index('HourDK')
for column in df.columns.to_list():
    df = df[df[column].apply(lambda x: isinstance(x,float))]
df.to_pickle(SaveDir + FileName + '.pkl')


# df = df.loc[df.TotalLoad.between(df.TotalLoad.rolling(window = '7D').mean() -
#                                  3*df.TotalLoad.rolling(window = '7D').std(),
#                                  df.TotalLoad.rolling(window = '7D').mean() +
#                                  3*df.TotalLoad.rolling(window = '7D').std())]
#
# df.plot()