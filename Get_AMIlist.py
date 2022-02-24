#!/usr/bin/env python
# Get AWS AMI owned by self (you) - change as appropriate
# Prints as Python Dictionary

import boto3

client = boto3.client(
    'ec2',
    aws_access_key_id="AKIAxxxxxxxx",
    aws_secret_access_key="xxxxxx",
    region_name="eu-west-1"
)
ec2 = boto3.client('ec2')
images = ec2.describe_images(Owners=['self'])
print(images)
