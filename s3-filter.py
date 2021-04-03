#!/usr/bin/env python3
# create with good vibes by: achgeek
# description: enable sse - s3 bucket

import boto3

profile = input("Insert your aws profile: ")

boto3.setup_default_session(profile_name=profile)

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    for obj in bucket.objects.filter(Prefix='neptune/'):
        print('{0}:{1}'.format(bucket.name, obj.key))