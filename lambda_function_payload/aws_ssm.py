import json
import boto3

client = boto3.client('ssm')

class SSM:

    def ssm_get_parameter(ssm_parameter_name):
        response = client.get_parameter(
            Name=ssm_parameter_name,
            WithDecryption=True
        )
        return response['Parameter']['Value']