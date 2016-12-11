# Elastic Beanstalk

This example shows how to host a simple static web site at AWS using
Elastic Beanstalk.

What does it do?

* It creates a new S3 bucket from which the Beanstalk app will load its
  site code and some config options.
* It copies the files from the "public" subdirectory to that bucket.
* It creates a new Beanstalk application and deploys it.
* It verifies that the site is functioning correctly, as reported by
  Elastic Beanstalk.
