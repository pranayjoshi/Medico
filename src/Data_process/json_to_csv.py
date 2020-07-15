import pandas as pd
from os import path
def filechecker(file_name):
    check = path.exists(file_name)
    return check
def converter(location):
    df = pd.read_json(r'./data/snomed_data.json')
    df.to_csv(location, index = None)
def run():
    file_loc = "./data/data.csv"
    if not filechecker(file_loc):
        converter(file_loc)
if __name__ == "__main__":
    run()
