#!/usr/bin/env python
# Set AWS Session Creds

import boto3

session = boto3.Session(
    aws_access_key_id="AKIxxxxxxxxxxxxxxxxx",
    aws_secret_access_key="xxxxxxxxxxxxxxxxx"
    )