from createTable import createTables
import jsonOperations
from GetData import download

def getSymbolsbyIndustry():
    object=download
    object.SymbolperIndustry()

def getSymbolsfromYahoo():
    object=download
    object.SymbolfromYahoo()

def getDatafromYahoo():
    object=download
    object.downloadDataFromYahoo()


def createTableAws():
    object=createTables()
    jsonFile=jsonOperations.loadJson("tablas.json")
    Symbol=jsonFile["Symbol"]
    for i in Symbol:
        object.pricesTable("table_with_symbol_{}".format(Symbol[i]))

def createTableSector():
    object=createTables
    object.SymbolByEconomicSectorTable()