#!/usr/bin/env python
# Get AWS key pair's for specified Region

import boto3

client = boto3.client(
    'ec2',
    aws_access_key_id="AKIAxxxxxxxx",
    aws_secret_access_key="xxxxxxx",
    region_name="eu-west-1"
)

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print(response)