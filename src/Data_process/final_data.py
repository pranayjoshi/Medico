import file_path as fp
import pandas as pd
from csv_pandas import csv_to_dataframe, df_to_csv

def get_file_path():
    initial_data = fp.run("initial_data")
    tokenized_data = fp.run("tokenized_data")
    main_data_loc = fp.run("main_data")
    return main_data_loc, initial_data, tokenized_data
    
class preprocess:

    def __init__(self, initial_data, tokenized_data):
        self.initial_data = initial_data
        self.tokenized_data = tokenized_data

    def tokenized_to_df(self):
        data_loc = self.tokenized_data
        tokenized_df = csv_to_dataframe(data_loc)
        self.tokenized_df = tokenized_df

    def initial_to_df(self):
        data_loc = self.initial_data
        initial_df = csv_to_dataframe(data_loc)
        self.initial_df = initial_df

    def concat_data(self):
        tokenized_df = self.tokenized_df
        initial_df = self.initial_df
        final_df = pd.concat([initial_df, tokenized_df])
        return final_df

def run_all_preprocess(initial_data, tokenized_data):
    pre_process = preprocess(initial_data, tokenized_data)
    pre_process.tokenized_to_df()
    pre_process.initial_to_df()
    final_df = pre_process.concat_data()
    return final_df

def df_to_maincsv(dataframe, csv_loc):
    df_to_csv(dataframe, csv_loc)

def run():
    main_data_loc, initial_data, tokenized_data = get_file_path()
    final_df = run_all_preprocess(initial_data, tokenized_data)
    df_to_maincsv(final_df, main_data_loc)
    return final_df

if __name__ == "__main__":
    print(run().head())
    print(run().shape)