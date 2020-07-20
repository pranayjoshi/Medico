import pandas as pd
from os import path
import file_path as fp
class processing:
    def __init__(self):
        pass
    def extract_file_paths(self):
        file_path = fp
        self.snomed_json_loc = file_path.run("snomed_json")
        self.data_loc = file_path.run("data")
    def create_dataframe(self):
        dataframe = pd.read_json(self.snomed_json_loc)
        self.df = dataframe
    def cloumn_to_delete(self):
        self.to_remove = "system"
    def delete_idx(self):
        self.df = self.df.drop(self.to_remove, axis=1)
    def converter(self):
        self.df.to_csv(self.data_loc, index = None)
class preprocess:
    def extract_file_paths(self):
        file_path = fp
        self.file_name = file_path.run("data")
    def filechecker(self):       
        check = path.exists(self.file_name)
        return check
class postprocess:
    def __init__(self):
        pass
    def runall_pre(self):
        self.pre_process = preprocess()
        self.pre_process.extract_file_paths()
        self.file_checker = self.pre_process.filechecker()
        return self.file_checker
    def runall_processing(self):
        process = processing()
        process.extract_file_paths()
        process.create_dataframe()
        process.cloumn_to_delete()
        process.delete_idx()
        process.converter()
def runall():
    post_process = postprocess()
    post_process.runall_processing()
