import json

def run(file_name):
    with open("./storage/path.json", "r+") as file:       #for mailing system
        data = json.load(file)
        location = data[file_name]
        return location
