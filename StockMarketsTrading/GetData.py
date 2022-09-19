import pandas as pd
import yfinance as yf
from stocksymbol import StockSymbol
from generate import generateClass
import jsonOperations



class download():
    
    def SymbolperIndustry():
        data=pd.read_excel("./generatedFiles/listado_de_empresas.xlsx")
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
        count=len(Symbol)
        Period=configData["Period"]
        Interval=configData["Interval"]
        data=yf.download(Symbol,period=Period,interval=Interval)
        objcsv=generateClass()
        objcsv.generateCSV(data)
        data_after=data.reset_index()      
        dict={}
        a=0
        list=[]
        for i in data_after:
            sub_dict={}
            if a%count==1:
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
        df=pd.DataFrame.from_dict(dict.items())
        jsonOut=df.to_json("tablas.json")

