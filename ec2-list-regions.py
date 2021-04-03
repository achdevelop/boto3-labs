#!/usr/bin/env python3
# create with good vibes by: achgeek
# description: enable sse - s3 bucket

import boto3

profile = input("Insert your aws profile: ")

boto3.setup_default_session(profile_name=profile)

response = boto3.resource(service_name="ec2")

for region in response.meta.client.describe_regions()['Regions']:
	print(region['RegionName'])