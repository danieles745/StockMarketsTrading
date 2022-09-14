import pandas as pd
import yfinance as yf
from stocksymbol import StockSymbol
import jsonOperations
import json


class download():
    
    def SymbolperIndustry():
        data=pd.read_excel("listado_de_empresas.xlsx")
        df=pd.DataFrame(data)
        # we define the keys
        Symbol=df['Symbol']
        Industry=df['Industry']

        # we build the dictionary
        ticks={"Symbol":Symbol,"Industry":Industry}



        # we convert the dict to json
        jsonOut=df.to_json("listado_de_empresas.json")

    def SymbolfromYahoo():
        api_key='5ee6c932-c90f-47ea-969c-b57b76437464'
        ss=StockSymbol(api_key)
        list_symbols=ss.get_symbol_list(market="US")
        df=pd.DataFrame(list_symbols)
        jsonOut=df.to_json("listado_de_tickers.json")
        jsonOut
    
    def downloadDataFromYahoo():
        configData=jsonOperations.loadJson("./config/config.json")
        Symbol=configData["Symbol"]
        Period=configData["Period"]
        Interval=configData["Interval"]
        dict={}
        for i in Symbol:
            ticker=yf.Ticker(i)
            dict[i]=ticker.history(period=Period,interval=Interval)
        data=pd.DataFrame(dict.items(),columns=["Symbol","Data"])
        jsonOut=data.to_json("tablas.json")

