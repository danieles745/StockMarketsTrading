import jsonOperations
import boto3
import json

class insert():

    def insertDataPerIndustry(self):
        client = boto3.client('dynamodb')
        configFile=jsonOperations.loadJson("listado_de_empresas.json")
        a=0
        for i in configFile["Symbol"]:
            response = client.put_item(
                TableName='StocksByEconomicSector',
                Item={
                    'NameTick': {
                        'S': configFile["Symbol"][i],
                    },
                    'EconomicSector': {
                        'S': configFile["Industry"][i],
                    }                    
                },  
            )
            if a==4:
                break
            a+=1


    def insertDataTickers(self):
        client = boto3.client('dynamodb')
        configFile=jsonOperations.loadJson("tablas.json")
        jsonFile=jsonOperations.loadJson("./config/config.json")
        Symbol=jsonFile["Symbol"]
        count=len(Symbol)        
        for i in Symbol:
            for e in range(count):
                for p in range(4):
                    di=list(configFile["1"]["1"][e])[0]

                    response = client.put_item(
                        TableName='table_with_symbol_{}'.format(i),

                        Item={
                            'Date': {
                                'S': configFile["1"]["0"][str(e)],
                            },
                            'Adj_Close': {
                                'S': configFile["1"]["1"][e][di][str(p)],
                            },
                            'Close': {
                                'S': configFile["1"]["2"][e][di][str(p)],
                            },
                            'High': {
                                'S': configFile["1"]["3"][e][di][str(p)],
                            },
                            'Low': {
                                'S': configFile["1"]["4"][e][di][str(p)],
                            },
                            'Open': {
                                'S': configFile["1"]["5"][e][di][str(p)],
                            },
                            'Volume': {
                                'S': configFile["1"]["6"][e][di][str(p)],
                            }                                                                                                                                                        
                        },  
                    )

    def insertDataSymbolDetails(self):
        client = boto3.client('dynamodb')
        configFile=jsonOperations.loadJson("listado_de_tickers.json")
        for i in range(4):
            response = client.put_item(
                TableName='TickersDetails',
                Item={
                    'symbol': {
                        'S': configFile["symbol"][str(i)],
                    },
                    'ShortName': {
                        'S': configFile["shortName"][str(i)],
                    },  
                    'LongName': {
                        'S': configFile["longName"][str(i)],
                    },
                    'Exchange': {
                        'S': configFile["exchange"][str(i)],
                    }, 
                    'Market': {
                        'S': configFile["market"][str(i)],
                    },
                    'QuoteType': {
                        'S': configFile["quoteType"][str(i)],
                    }                                                            
                },  
            )
