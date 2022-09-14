import json
import os

def loadJson(filepath):
    blank_json={}
    if os.path.exists(filepath):
        try:
            f=open(filepath,"r")
            data=json.load(f)
            f.close()
            return data
        except ValueError:
            print("path doesnt exist")
            return blank_json
    else:
        return blank_json
