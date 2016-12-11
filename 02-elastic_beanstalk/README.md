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

Assumptions:

* This was written on macOS 10.12, but it should work on any UNIX-like
  system that has the "uuidgen" command.
* It runs under ksh, and uses some conveniences that are unique to that
  shell.
* It uses the [AWS CLI](https://aws.amazon.com/documentation/cli/). On a
  Mac, that's easy to install using [Homebrew](http://brew.sh).
* You have API access to your AWS account, and you've configured the
  AWS CLI tools to use it.
