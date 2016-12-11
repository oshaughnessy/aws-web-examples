# Hosting a web site at Elastic Beanstalk using the AWS CLI

This example shows how to host a web site at AWS using
[Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).
That platform is capable of much more than is shown here, but this
script illustrates how to deploy an application to it using the
[AWS CLI](https://aws.amazon.com/documentation/cli/) tools.

What does it do?

* It creates a new [S3](https://aws.amazon.com/s3/) bucket, from which
  the Beanstalk app will load its site code and some config options.
* It copies the files from the local "public" subdirectory to that bucket.
* It creates a new Beanstalk application, using as many defaults as
  possible, then deploys it. The application is deployed on a
  [single t2.nano instance](./public/.ebextensions/launch.config).
* It verifies that the site is functioning correctly, as reported by
  Elastic Beanstalk's own health check system.

Assumptions:

* This was written on macOS 10.12, but it should work on any UNIX-like
  system that has the "uuidgen" command.
* It runs under ksh, and uses some conveniences that are unique to that shell.
* It uses the AWS CLI. On a Mac, that's easy to install using
  [Homebrew](http://brew.sh).
* You have API access to your AWS account, and you've configured the
  AWS CLI tools to use it.
