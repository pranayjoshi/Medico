import pandas as pd
import sys
sys.path.append('./src/AI_files')
import stopwords_tokenizer as rem_stopwords
import file_path as fp

class list_to_csv:
    def __init__(self, feature_list, csv_location):
        self.feature_list = feature_list
        self.csv_location = csv_location

    def list_to_series(self):
        series = pd.Series(self.feature_list)
        self.series = series

    def series_to_csv(self):   
        series = self.series
        series.to_csv(self.csv_location)

def get_loc():
    csv_location = fp.run("tokenized_data")
    return csv_location

def runall(feature_list,csv_location):
    list2csv = list_to_csv(feature_list,csv_location)
    list2csv.list_to_series()
    list2csv.series_to_csv()

def run():
    feature_list = rem_stopwords.run()
    csv_location = get_loc()
    runall(feature_list,csv_location)
    
if __name__ == "__main__":
    run()


        


