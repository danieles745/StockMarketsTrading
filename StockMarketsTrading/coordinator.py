from createTable import createTables
import jsonOperations
from GetData import download
from insertData import insert
from delete import delete
import time
# This method will get symbols per economic sector and will host them in json file
# 
# ok
def getSymbolsbyIndustry():
    object=download
    object.SymbolperIndustry()
# ok
def getSymbolsfromYahoo():
    object=download
    object.SymbolfromYahoo()
# ok 
def getDatafromYahoo():
    object=download
    object.downloadDataFromYahoo()

# ok
def createTableAws():
    object=createTables()
    jsonFile=jsonOperations.loadJson("./config/config.json")
    Symbol=jsonFile["Symbol"]
    for i in Symbol:
        object.pricesTable("table_with_symbol_{}".format(i))

# ok
def createTableSector():
    object=createTables()
    object.SymbolByEconomicSectorTable()


# ok
def SymbolfromYahoo():
    object=createTables()
    object.SymbolfromYahoo()

# ok
def insertDataPerIndustry():
    object=insert()
    object.insertDataPerIndustry()



# ok
def insertDataTickers():
    object=insert()
    object.insertDataTickers()

# ok
def insertDataSymbolDetails():
    object=insert()
    object.insertDataSymbolDetails()


# ok
def deleteDataPerIndustry():
    object=delete()
    object.deleteDataPerIndustry()

# ok
def deleteDataTickers():
    object=delete()
    object.deleteDataTickers()


def deleteDataTickerDetails():
    object=delete()
    object.deleteDataTickerDetails()




def insertData():
    insertDataPerIndustry()
    insertDataTickers()
    insertDataSymbolDetails()

def deleteTables():
    deleteDataPerIndustry()
    deleteDataTickers()
    deleteDataTickerDetails()




# if __name__=='__main__':
#     getSymbolsbyIndustry()
#     getSymbolsfromYahoo()
#     getDatafromYahoo()
#     createTableAws()
#     createTableSector()
#     SymbolfromYahoo()
#     print("Proceso ejecutado satisfactoriamente. Las tablas se han creado")
#     time.sleep(10)
#     insertData()



if __name__=='__main__':
    deleteTables()

