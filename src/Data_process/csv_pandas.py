import pandas as pd
def readcsv(csv_loc):
    csv = pd.read_csv(csv_loc)
    return csv
def csv_to_series(csv_loc):
    csv = readcsv(csv_loc)
    series = pd.series(csv)
    return series
def csv_to_dataframe(csv_loc):
    csv = readcsv(csv_loc)
    dataframe = pd.DataFrame(csv)
    return dataframe
def df_to_csv(dataframe, location):
    dataframe.to_csv(location, index=False)

