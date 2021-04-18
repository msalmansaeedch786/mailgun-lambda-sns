"""This module stores data in AWS S3"""
import boto3

client = boto3.client('s3')

class S3:
    """AWS S3 Client"""

    def s3_store(self, body, bucket_name, key_name):
        """stores the raw webhook using put_object method"""
        response = client.put_object(
            Body=body,
            Bucket=bucket_name,
            Key=key_name
        )
        return response
