import boto3
import json

def lambda_handler(event):
    # TODO implement
    tables=event[0]
    print(tables)
    return {
        'statusCode': 200,
        'body': tables,
        }


def datacollect(table):
    client = boto3.client('dynamodb')
    response = client.scan(
    TableName="table_with_symbol_{}".format(table),
    )
    return response

