import json
import boto3
import uuid
import os

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
sqs = boto3.client('sqs')

# Environment variables (configured during Lambda deployment)
TABLE_NAME = os.environ.get('TABLE_NAME', 'AppItems')
QUEUE_URL = os.environ.get('QUEUE_URL', '')

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # 1. Parse JSON body
        body = json.loads(event.get('body', '{}'))
        item_id = body.get('id', str(uuid.uuid4()))
        message_content = body.get('message', 'Default serverless message')

        # 2. Store item in DynamoDB
        table.put_item(Item={
            'id': item_id,
            'message': message_content
        })

        # 3. Offload asynchronous job to SQS (if configured)
        if QUEUE_URL:
            sqs.send_message(
                QueueUrl=QUEUE_URL,
                MessageBody=json.dumps({
                    'id': item_id,
                    'task': 'SEND_NOTIFICATION',
                    'message': message_content
                })
            )

        # 4. Return success response with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'status': 'Success',
                'id': item_id,
                'message': 'Record stored and task queued successfully'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }