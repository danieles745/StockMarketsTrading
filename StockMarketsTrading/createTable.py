import boto3

class createTables():


    def SymbolByEconomicSectorTable(self):
        client = boto3.client('dynamodb')
        response = client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'NameTick',
                    'AttributeType': 'S'
                },
            ],
            TableName='StocksByEconomicSector',
            KeySchema=[
                {
                    'AttributeName': 'NameTick',
                    'KeyType': 'HASH'
                },
            ],
            BillingMode='PAY_PER_REQUEST',
        )

    def pricesTable(self,NameTable):

        client = boto3.client('dynamodb')
        response = client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'Date',
                    'AttributeType': 'S'
                },
            ],
            TableName=NameTable,
            KeySchema=[
                {
                    'AttributeName': 'Date',
                    'KeyType': 'HASH'
                },
            ],
            BillingMode='PAY_PER_REQUEST',
        )        