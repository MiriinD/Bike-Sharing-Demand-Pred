import pandas as pd

def wrangle_open_meteo(open_meteo_df):
    weather_columns = {
        'time': 'hour', 
        'temperature_2m_(°c)': 'temperature_C', 
        'relative_humidity_2m_(%)': 'rel_humidity_perc',
        'apparent_temperature_(°c)': 'feels_like_temp_C', 
        'rain_(mm)': 'rain_mm',
        'cloud_cover_(%)': 'cloud_cover_perc', 
        'wind_speed_10m_(km/h)': 'wind_speed_kmh',
        'is_day_()':'is_day'
    }
    open_meteo_df.columns = [name.strip().replace(" ", "_").lower() for name in open_meteo_df.columns]
    open_meteo_df.rename(columns=weather_columns, inplace=True)
    
    # reformat the hour column to match our aggregated ecobici df and set as index
    open_meteo_df['hour'] = pd.to_datetime(open_meteo_df['hour'], format='%Y-%m-%dT%H:%M')
    open_meteo_df.set_index('hour', inplace=True)
    
    return open_meteo_df

def SARIMA_train_test_split(df, test_percentage): # df = dataframe, test_percentage = proportion of df we want to keep for testing
    n_test = int(round(len(df)*test_percentage, 0))
    train = df.iloc[:-n_test]
    test = df.iloc[-n_test:]
    return train, test