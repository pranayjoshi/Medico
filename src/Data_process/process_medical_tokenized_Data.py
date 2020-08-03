import pandas as pd
import file_path
from csv_pandas import readable_data_to_df, csv_to_dataframe,df_to_csv, readcsv_without_header
def get_filepath():
    tokenized_data_loc = file_path.run("tokenized_data")
    ini_data_loc = file_path.run("initial_data")
    return ini_data_loc, tokenized_data_loc
class preprocess:
    def __init__(self, ini_data_loc,tokenized_data_loc):
        self.tokenized_data_loc = tokenized_data_loc
        self.ini_data_loc = ini_data_loc
    def tokenized_data_to_readable(self):
        t_data_readable = readcsv_without_header(self.tokenized_data_loc)
        self.t_data_readable = t_data_readable
    def add_heading(self):
        data = self.t_data_readable
        data.columns = ["srno", "display",]
        self.t_data_readable = data
    def readable_data_to_df(self):
        tokenized_data_df = readable_data_to_df(self.t_data_readable)
        self.tokenized_data_df =  tokenized_data_df
    def data_to_dataframe(self):
        ini_data_df = csv_to_dataframe(self.ini_data_loc)
        self.ini_data_df =  ini_data_df
    def create_dataframe(self):
        ini_data_df = self.ini_data_df
        code = ini_data_df.code
        self.initial_dataframe = pd.DataFrame(code)
    def add_tokenized_data(self):
        initial_data = self.initial_dataframe
        tokenized_data_df = self.tokenized_data_df["display"]
        print(tokenized_data_df[:5])
        initial_data['display'] = tokenized_data_df
        self.tokenized_data = initial_data
    def run(self):
        tokenized_data = self.tokenized_data
        print(tokenized_data[:5])
        return tokenized_data
def runall_pre(ini_data_loc, tokenized_data_loc):
    pre_process = preprocess(ini_data_loc,tokenized_data_loc)
    pre_process.tokenized_data_to_readable()
    pre_process.add_heading()
    pre_process.readable_data_to_df()
    pre_process.data_to_dataframe()
    pre_process.create_dataframe()
    pre_process.add_tokenized_data()
    tokenized_data = pre_process.run()
    return tokenized_data
def process(tokenized_data, location):
    df_to_csv(tokenized_data, location)
def run():
    ini_data_loc, tokenized_data_loc = get_filepath()
    tokenized_data = runall_pre(ini_data_loc, tokenized_data_loc)
    process(tokenized_data, tokenized_data_loc)
if __name__ == "__main__":
    run()



