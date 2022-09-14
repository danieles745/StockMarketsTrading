import boto3

class createTables():


    def SymbolByEconomicSectorTable():
        client = boto3.client('dynamodb', aws_access_key_id= '', aws_secret_access_key='')
        response = client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'NameTick',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'EconomicSector',
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
            TableClass='STANDARD'|'STANDARD_INFREQUENT_ACCESS'
        )

    def pricesTable(self,NameTable):

        client = boto3.client('dynamodb', aws_access_key_id= '', aws_secret_access_key='')
        response = client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'Date',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'Open',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'High',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'Low',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'Close',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'AdjClose',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'Volume',
                    'AttributeType': 'N'
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
            TableClass='STANDARD'|'STANDARD_INFREQUENT_ACCESS'
        )        