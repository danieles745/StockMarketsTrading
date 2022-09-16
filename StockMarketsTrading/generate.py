import jsonOperations
import pandas as pd
import json

class generateClass():
    def generateCSV(self):
        jsonFile=jsonOperations.loadJson("./tablas.json")
        jsonF=json.dumps(jsonFile)
        df=pd.read_json(jsonF)
        csv_data=df.to_csv("./data.csv")