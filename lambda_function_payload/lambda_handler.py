import os
import json
import hashlib, hmac

from aws_s3 import S3
from aws_sns import SNS
from aws_ssm import SSM

def lambda_handler(event, context):
    # TODO implement
    
    result = json.loads(event['body'])
    print(result)
    
    token = result['signature']['token']
    timestamp = result['signature']['timestamp']
    signature = result['signature']['signature']
    mailgun_event = result['event-data']['event']

    message = {
        "Provider"  : "Mailgun",
        "timestamp" : timestamp,
        "type"      : "email " + str(mailgun_event)
    }

    # extracting the requried values coming from the mailgun event
    webhook_signing_key = SSM.ssm_get_parameter(os.environ['webhook_signing_key'])
    s3_bucket_name = os.environ['s3_bucket_name']
    sns_topic_arn = os.environ['sns_topic_arn']
    
    if verify(webhook_signing_key, token, timestamp, signature):
        
        # storing raw webhook in AWS S3 data store
        S3.s3_store(json.dumps(result), s3_bucket_name, 'raw_webhook_'+str(timestamp)+'.json')

        # publishing transformed webhook via AWS SNS service
        SNS.sns_publish(sns_topic_arn, message)

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
    hmac_digest = hmac.new(key=signing_key.encode(),
                           msg=('{}{}'.format(timestamp, token)).encode(),
                           digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(str(signature), str(hmac_digest))