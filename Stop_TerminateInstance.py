#!/usr/bin/env python3

import boto3

AWS_REGION = "eu-west-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-xxxxxxxxxxxxxxx'

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

instance.terminate()

print(f'Terminating EC2 instance: {instance.id}')
    
instance.wait_until_terminated()

print(f'EC2 instance "{instance.id}" has been terminated')