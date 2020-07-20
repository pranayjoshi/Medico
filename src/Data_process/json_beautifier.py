import json
import file_path as f_p
class beautify:
    def __init__(self, input_location, output_location):
        self.input_location = input_location
        self.output_location = output_location
    def json_to_dict(self):
        with open(self.input_location) as f:
            json_object = json.load(f)
        self.json_object = json_object
    def json_beautifier(self):
        converted_dict = json.dumps(self.json_object, indent=2)
        self.converted_dict = converted_dict
    def exporter(self):
        with open(self.output_location, "w") as outfile: 
            outfile.write(self.converted_dict) 
def run_all(input_location, output_location):
    beautify_class = beautify(input_location, output_location)
    beautify_class.json_to_dict()
    beautify_class.json_beautifier()
    beautify_class.exporter()

if __name__ == "__main__":
    run()

