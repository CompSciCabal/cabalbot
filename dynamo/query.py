import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Diversions')

def diversion_for_week(date):
    """Returns a list of diversions for the given date. date can be 'unscheduled' or of the form 'YYYY-MM-DD'."""
    resp = table.query(KeyConditionExpression=Key('WeekOf').eq(date))
    return resp['Items']

def diversion_for_week_paper(date, paperURI):
    """Returns an object containing information for the specified date and paper. date can be 'unscheduled' or of the form 'YYYY-MM-DD'."""
    resp = table.get_item(Key={"WeekOf": date, "Paper": paperURI})
    return resp['Item']
