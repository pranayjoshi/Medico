import os 
import json

def status(loc):
    stat = os.stat(loc).st_size == 0
    return stat

def run():
    with open("./storage/path.json", "r+") as file:       #for mailing system
        data = json.load(file)
    loc = data["results"]
    return status(loc)
