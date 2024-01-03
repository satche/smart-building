import boto3
import os

# AWS
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION = os.environ['AWS_REGION']
TABLE_NAME = os.environ['TABLE_NAME']

# Create a DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Specify the name of your DynamoDB table
table = dynamodb.Table(TABLE_NAME)


def send_dummy_data():
    # Dummy data
    light_level = 250
    room_temperature = 22

    # Send the light level to the DynamoDB table
    table.put_item(
        Item={
            'knx-partition': 'light_level',
            'knx-key': str(light_level)
        }
    )

    # Send the room temperature to the DynamoDB table
    table.put_item(
        Item={
            'knx-partition': 'room_temperature',
            'knx-key': str(room_temperature)
        }
    )


send_dummy_data()
