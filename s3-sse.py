#!/usr/bin/env python3
# create with good vibes by: achgeek
# description: enable sse - s3 bucket

import boto3

# session and connection
boto3.setup_default_session(profile_name='foo')
s3 = boto3.resource('s3')
client = boto3.client('s3')

# test connection
# for bucket in client.buckets.all():
#     print(bucket.name)

for bucket in s3.buckets.all():

  # filter by region using: == 'eu-west-1' or != 'eu-west-1'
  if client.get_bucket_location(Bucket=bucket.name)['LocationConstraint'] == 'eu-west-1':
    # you could write in a file the bucket name
    print(bucket.name)
    response = client.put_bucket_encryption(
      Bucket=bucket.name,
      ServerSideEncryptionConfiguration={
        'Rules': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'
                }
            },
        ]
      }
   )