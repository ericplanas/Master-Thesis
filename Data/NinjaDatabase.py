import pandas as pd

SourceDir = 'C:/Users/PC/Desktop/Master Thesis/Data/Ninja/'
Hourly_Weather_NINJA = pd.read_csv(SourceDir + 'ninja_weather_country_DK_merra-2_land_area_weighted.csv')
Hourly_WindNUTS_NINJA = pd.read_csv(SourceDir + 'ninja_wind_country_DK_current_merra-2_nuts-2_corrected.csv')
Hourly_PVNUTS_NINJA = pd.read_csv(SourceDir + 'ninja_pv_country_DK_merra-2_nuts-2_corrected.csv')

def DefineSettings():

    Settings = {}
    Settings['DateRange'] = ['2018-01-01','2020-01-01']

    return Settings
def CleanNINJAData(df, daterange):
    df.columns = df.iloc[1]
    df = df.drop(index=[0, 1])
    df.time = pd.to_datetime(df.time, format='%Y-%m-%d %H:%M:%S')
    df = df[(df.time > pd.Timestamp(daterange[0]))]
    return df

Settings = DefineSettings()
Hourly_Weather_NINJA = CleanNINJAData(Hourly_Weather_NINJA, Settings['DateRange'])
Hourly_WindNUTS_NINJA = CleanNINJAData(Hourly_WindNUTS_NINJA, Settings['DateRange'])
Hourly_PVNUTS_NINJA = CleanNINJAData(Hourly_PVNUTS_NINJA, Settings['DateRange'])

print('a')
