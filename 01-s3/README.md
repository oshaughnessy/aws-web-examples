# Hosting a static web site at AWS using S3

This example shows how to host a simple static web site at AWS using 
[Amazon S3](https://aws.amazon.com/s3/), their Simple Storage Service,
and [Boto3](https://aws.amazon.com/sdk-for-python/), their SDK for Python.

What does it do?

* It creates a new S3 bucket with the web hosting feature enabled.
* It copies the files from the "public" subdirectory to the bucket.
* It gives you back the URL to the new site.
* It verifies that it's accessible over HTTP.

There are more sophisticated ways to host a web site in S3.
You can run the site under your own domain, with or without using
[Route 53](https://aws.amazon.com/route53/). You can use the
[CloudFront](https://aws.amazon.com/cloudfront/) CDN (or others) to
improve performance, reduce cost, and use SSL. This just shows a way
to use S3 with Python.

Assumptions:

* You have [boto3](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation) installed.
* You have API access to your AWS account and you've configured your
  local user account to use it.
