#!/usr/local/bin/python

'''
static-s3

A simple, naive script that sets up static web hosting at S3.

It creates an S3 bucket with a random name (using a UUID), then copies
all the files from the local "public" subdir to the bucket. Finally,
static web hosting is enabled on the bucket.

The script assumes that the file "public/index.html" exists.
'''

# Boto is Amazon's Python SDK for AWS
# https://boto3.readthedocs.io/en/latest/index.html
import boto3

import mimetypes
import os
import re
import requests
import sys
import uuid

# Get a handle to manage our new S3 bucket.
s3 = boto3.resource('s3')

# Generate a random name for the bucket.
bucket_name = str(uuid.uuid4())

# Create the bucket, exiting if we get an error.
bucket = s3.Bucket(bucket_name)
try:
    response = bucket.create(ACL='public-read')
except botocore.exceptions.ClientError as e:
    error_code = int(e.response['Error']['Code'])
    print "ERROR:", e.response
    sys.exit(1)

# Get the website-management handle for our new bucket
website = s3.BucketWebsite(bucket_name)
website.put(
    WebsiteConfiguration = {
        'IndexDocument': { 'Suffix': 'index.html' }
    }
)

# Upload all the files from the "public" subdirectory into the bucket.
# Note that we have to identify the mime-type of each file so that
# we can define its Content-Type header for S3.
os.chdir('public')
mimetypes.init()
print "Uploading public files....\n"
for dirpath, dirnames, filenames in os.walk('.'): 
    for f in filenames:
        # Strip the base parent directory from the path, or S3 will
        # put it all in a subdir called ".".
        key_name = re.sub(r'^./', '', os.path.join(dirpath, f))
        local_file = os.path.join(dirpath, f)
        print "    {}".format(local_file)
        (file_type, encoding) = mimetypes.guess_type(local_file)
        bucket.upload_file(local_file, key_name,
                           ExtraArgs = {
                               'ACL':         'public-read',
                               'ContentType': file_type
                           }
                          )
print ""

# Ask Amazon for the canonical URL to the bucket's index file.
# Since we made the site publicly accessible, we don't need the presigned
# credentials, but this is a convenient way to get the base URL.
# NOTE: We're assuming that the public subdir includes an "index.html" file.
url = boto3.client('s3').generate_presigned_url(
          ClientMethod='get_object',
          Params={
              'Bucket': bucket_name,
              'Key': 'index.html'
          }
      )

# Use HTTP to get the new site's index file, then verify that it worked.
r = requests.get(url)
if r.status_code == 200:
    clean_url = re.split(r'\?', url)[0]
    print "Tested! You can access your new site at:\n"
    print "    {}\n".format(clean_url)
    print "Try it yourself from the shell:\n"
    print "    curl -ski -o- {}\n".format(clean_url)
else:
    print "Oops. Something went wrong.\n"
    print r.raise_for_status()
