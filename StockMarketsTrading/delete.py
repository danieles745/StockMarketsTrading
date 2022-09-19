import boto3
import jsonOperations

class delete():

    def deleteDataPerIndustry(self):
        client = boto3.client('dynamodb')
        response = client.delete_table(
            TableName='StocksByEconomicSector'
        )

    def deleteDataTickers(self):
        client = boto3.client('dynamodb')
        jsonFile=jsonOperations.loadJson("./config/config.json")
        Symbol=jsonFile["Symbol"]
        for i in Symbol:       
            response = client.delete_table(
                TableName="table_with_symbol_{}".format(i)
        )                

    def deleteDataTickerDetails(self):
        client = boto3.client('dynamodb')
        response = client.delete_table(
            TableName='TickersDetails'
        )    