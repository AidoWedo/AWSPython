#!/usr/bin/env python
# Get AWS AMI owned by self (you) - change as appropriate
# Prints as Python Dictionary

import boto3

AWS_REGION = "eu-west-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
KEY_PAIR_NAME = 'Automation'
AMI_ID = 'ami-xxxxxxx'
SUBNET_ID = 'subnet-xxxxxxx'

instances = EC2_RESOURCE.create_instances(
    MinCount = 1,
    MaxCount = 1,
    ImageId=AMI_ID,
    InstanceType='t2.micro',
    KeyName=KEY_PAIR_NAME,
    SubnetId='subnet-xxxxxx')
for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    
    instance.wait_until_running()
    print(f'EC2 instance "{instance.id}" has been started')