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
    
    def downloadDataFromYahoo():
        configData=jsonOperations.loadJson("./config/config.json")
        Symbol=configData["Symbol"]
        Period=configData["Period"]
        Interval=configData["Interval"]
        data=yf.download(Symbol,period=Period,interval=Interval)
        data_after=data.reset_index()
        dict={}
        a=0
        for i in data_after:
            sub_dict={}
            if a%2!=0:
                list=[]
            if a>0:
                sub_dict[i[1]]=data_after[i]
                df1=pd.DataFrame.from_dict(sub_dict)
                df1=df1.astype(str)
                list.append(df1)
                dict[i[0]]=list
            else:
                dict[i[0]]=data_after[i]
            a+=1
        dict["Date"]=dict["Date"].astype(str)
        print(dict)
        df=pd.DataFrame.from_dict(dict.items())
        jsonOut=df.to_json("tablas.json")
        # data_dict=json.dumps(dict)
        # jsonOut=data_dict.to_json("tablas.json")
        # 
        # for i in Symbol:
        #     ticker=yf.Ticker(i)
        #     df=ticker.history(period=Period,interval=Interval)
        #     Open=df["Date"]
        #     print(Open)
            # values=df.to_dict()
            # # print(values)
            # dict[i]=values
            
            # data=json.dumps(dict)
            # print(data)
        # data=pd.DataFrame(columns=["Symbol","Data"])
        # jsonOut=data.to_json("tablas.json")

