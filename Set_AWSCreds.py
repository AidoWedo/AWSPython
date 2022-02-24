#!/usr/bin/env python
# Set Creds and Region with Boto3, creates two clients one for IAM and one for ec2

import boto3

client = boto3.client(
    'iam',
    aws_access_key_id="AKIAxxxxxxx",
    aws_secret_access_key="xxxxxxxxx",
    region_name="eu-west-1"
)
client = boto3.client(
    'ec2',
    aws_access_key_id="AKIAxxxxxxxxxxxxxxx",
    aws_secret_access_key="xxxxxxxxxxxxxxxxxxx",
    region_name="eu-west-1"
)
