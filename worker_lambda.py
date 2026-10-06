import json

def lambda_handler(event, context):
    """Processes messages delivered asynchronously from the SQS queue."""
    for record in event.get('Records', []):
        body = json.loads(record['body'])
        print(f"Worker processing task for Item ID: {body.get('id')}")
        print(f"Task type: {body.get('task')}, Content: {body.get('message')}")
        # Add your email notification or background logic here
        
    return {'status': 'Batch processed'}