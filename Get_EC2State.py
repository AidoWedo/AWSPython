#!/usr/bin/env python3

import boto3

AWS_REGION = 'eu-west-1'
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-xxxxxxxxx'

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

print(f'EC2 instance "{INSTANCE_ID}" state: {instance.state["Name"]}')