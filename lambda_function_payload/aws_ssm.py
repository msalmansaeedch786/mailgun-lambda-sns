"""This module fetch a parameter from AWS SSM"""
import boto3

client = boto3.client('ssm')

class SSM:
    """AWS SSM Client"""

    def ssm_get_parameter(self, ssm_parameter_name):
        """get the parameter using get_parameter method"""
        response = client.get_parameter(
            Name=ssm_parameter_name,
            WithDecryption=True
        )
        return response['Parameter']['Value']
