#!/usr/bin/env python3
# create with good vibes by: achgeek
# description: list all buckets - s3 bucket

import boto3

profile = input("Insert your aws profile: ")

boto3.setup_default_session(profile_name=profile)
# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')