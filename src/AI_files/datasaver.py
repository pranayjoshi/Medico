import json
import os
a = input("enter the recipient's name: ")
b = input(f"enter {a}'s patient-id: ")
dic = {}
dic[a] = b
try:
    with open("./storage/patient_list.json", "r+") as file:
        data = json.load(file)
        if next(iter(dic)) not in data.keys():
            data.update(dic)
            file.seek(0)
            json.dump(data, file)
            print(data)
        else:
            print("the patient's name is already registered.\do you want to overwrite it.")
            s = input()
            s.lower()
            if "y" in s:
                data.update(dic)
                file.seek(0)
                json.dump(data, file)
                print(data)
            elif "n" in s:
                print("Okay!")
            else:
                print("not recognised")
except FileNotFoundError as fe:
    with open("mailing_list.json", "w+") as file:
        json.dump(dic, file)