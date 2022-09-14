import boto3

client = boto3.client('dynamodb')


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