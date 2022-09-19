import pandas as pd

class generateClass():
    def generateCSV(self,dataframe):
        dataframe.to_csv("./generatedFiles/data.csv")