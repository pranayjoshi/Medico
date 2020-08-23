import file_path 
import json_beautifier
import json_to_csv

class dataprocess_run:
    def json_beautify():
        run_beutifier = json_beautifier
        input_location = file_path.run("snomed_raw")
        output_location = file_path.run("snomed_json")   
        run_beutifier.run_all(input_location, output_location)

    def json2csv():
        json_2_csv = json_to_csv
        post_process = json_2_csv.postprocess()
        filechecker =  post_process.runall_pre()
        if not filechecker:
            json_2_csv.runall()
        else:
            dec = input("The dataset is already created. Do you want to overwrite the dataset?")
            dec = dec.lower()
            if "y" in dec:
                json_2_csv.runall()
               
def run():
    dataprocess_run.json_beautify()
    dataprocess_run.json2csv()
run()

