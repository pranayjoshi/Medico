import pandas as pd
import json
import filepath as fp
def read_csv(csv_loc):
    readcsv = pd.read_csv(csv_loc)
    return readcsv
def dataframe(csv):
    data_frame = pd.DataFrame(csv)
    return data_frame
def get_file_path():
    data_loc = fp.run("initial_data")
    return data_loc
def run():
    csv_loc = get_file_path()
    csv = read_csv(csv_loc)
    return dataframe(csv)
