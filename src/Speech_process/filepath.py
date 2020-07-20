# importing from parents directroy

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Data_process import file_path as f_p

def run(file_name):
    filepath = f_p.run(file_name)
    return filepath

