import pandas as pd

def readcsv(csv_loc):
    csv = pd.read_csv(csv_loc)
    return csv

def readcsv_without_header(csv_loc):
    csv = pd.read_csv(csv_loc,header=None)
    return csv

def csv_to_series(csv_loc):
    csv = readcsv(csv_loc)
    series = pd.series(csv)
    return series

def readable_data_to_df(readable_data):
    dataframe = pd.DataFrame(readable_data)
    return dataframe

def csv_to_dataframe(csv_loc):
    csv = readcsv(csv_loc)
    dataframe = pd.DataFrame(csv)
    return dataframe
    
def df_to_csv(dataframe, location):
    dataframe.to_csv(location, index=False)

