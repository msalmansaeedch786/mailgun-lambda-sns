import json
import boto3

client = boto3.client('sns')

class SNS:

    def sns_publish (topic_arn, message):
        response = client.publish(
            TopicArn=topic_arn,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )