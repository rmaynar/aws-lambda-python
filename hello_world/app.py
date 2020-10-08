import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    method = event['httpMethod']

    if method == 'GET':
        first_num = int(event['queryStringParameters']['first_num'])
        second_num = int(event['queryStringParameters']['second_num'])
        operator = event['queryStringParameters']['operator']
    elif method == 'POST':
        body = json.loads(event['body'])
        first_num = body['first_num']
        second_num = body['second_num']
        operator = body['operator']

    return {
        "statusCode": 200,
        "body": json.dumps(calc(first_num,second_num,operator)),
    }


def calc(first_num, second_num, operator):
    if operator == 'add':
        return first_num + second_num
    elif operator == 'substract':
        return first_num - second_num
    elif operator == 'multiply':
        return first_num * second_num
    elif operator == 'divide':
        if second_num != 0:
            return first_num / second_num

    return 0
