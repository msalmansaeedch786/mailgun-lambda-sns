"""This is the main lambda function handler"""
import os
import hmac
import json
import hashlib

from aws_s3 import S3
from aws_sns import SNS
from aws_ssm import SSM

def lambda_handler(event, _context):
    """This function will stores data in AWS S3, publish message using AWS SNS after verification"""

    # initializing clients
    s3 = S3()
    sns = SNS()
    ssm = SSM()

    result = json.loads(event['body'])
    print(result)

    # extracting requried values coming from the mailgun event
    token = result['signature']['token']
    timestamp = result['signature']['timestamp']
    signature = result['signature']['signature']
    mailgun_event = result['event-data']['event']

    # formatting message to be send to SNS endpoints
    message = {
        "Provider": "Mailgun",
        "timestamp": timestamp,
        "type": "email " + str(mailgun_event)
    }

    # getting the parameters from the environment to be passed to different functions
    webhook_signing_key = ssm.ssm_get_parameter(os.environ['webhook_signing_key'])
    s3_bucket_name = os.environ['s3_bucket_name']
    sns_topic_arn = os.environ['sns_topic_arn']

    if verify(webhook_signing_key, token, timestamp, signature):

        # storing raw webhook in AWS S3 data store
        s3.s3_store(
            json.dumps(result),
            s3_bucket_name,
            'raw_webhook_' +
            str(timestamp) +
            '.json')

        # publishing transformed webhook via AWS SNS service
        sns.sns_publish(sns_topic_arn, message)

    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid Signing Key for the Webhook')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda Executed Successfully!')
    }

def verify(signing_key, token, timestamp, signature):
    """This function will verify the Signin_Key for mailgun raw webhook events"""
    hmac_digest = hmac.new(key=signing_key.encode(),
                           msg=('{}{}'.format(timestamp, token)).encode(),
                           digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(str(signature), str(hmac_digest))
