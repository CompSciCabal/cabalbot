import boto3

client = boto3.client('dynamodb', region_name='us-east-2')

try:
    resp = client.create_table(
        TableName="Diversions",
        KeySchema=[
            {
                "AttributeName": "WeekOf",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Paper",
                "KeyType": "RANGE"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "WeekOf",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Paper",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print(resp)
except Exception as e:
    print(e)
