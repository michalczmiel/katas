import os
import json

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["VISIT_TABLE_NAME"])


def lambda_handler(event, context):
    """
    Lambda handler for registering new visits to the site
    """

    response = table.update_item(
        Key={
            'total': 0,
        },
        UpdateExpression="set total = total + :val",
        ExpressionAttributeValues={
            ':val': 1
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({})
    }
