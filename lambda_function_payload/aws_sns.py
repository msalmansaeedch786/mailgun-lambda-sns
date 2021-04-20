"""This module publish message using AWS SNS"""
import json
import boto3

class SNS:
    """AWS SNS Client"""

    def sns_publish(self, topic_arn, message):
        """deliver the message using publish method"""
        client = boto3.client('sns')
        response = client.publish(
            TopicArn=topic_arn,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        return response
