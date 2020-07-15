import json
def json_to_dict(input_location):
    with open('./data/snomed-sample-data-raw.json') as f:
        json_object = json.load(f)
    return json_object
def json_beautifier(json_object):
    converted_dict = json.dumps(json_object, indent=2)
    return converted_dict
def exporter(converted_dict, output_location):
    with open(output_location, "w") as outfile: 
        outfile.write(converted_dict) 
def run():
    input_location = './data/snomed-sample-data-raw.json'
    output_location = './data/snomed_data.json'
    json_object = json_to_dict(input_location)
    converted_dict = json_beautifier(json_object)
    exporter(converted_dict, output_location)
if __name__ == "__main__":
    run()

