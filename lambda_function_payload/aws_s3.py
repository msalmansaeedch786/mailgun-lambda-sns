import json
import boto3

client = boto3.client('s3')

class S3:

    def s3_store (body, bucket_name, key_name):
        response = client.put_object(
            Body=body, 
            Bucket=bucket_name, 
            Key=key_name
        )