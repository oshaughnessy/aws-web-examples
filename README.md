# aws-web-examples

Ways to host web sites at AWS


## Requirements

The AWS examples here require an account with
[Amazon Web Services](https://aws.amazon.com/).
The Vagrant examples could be used to deploy to AWS using
[vagrant-aws](https://github.com/mitchellh/vagrant-aws/).

You'll also need [AWS API](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/) credentials set up.

Other requirements are noted below.


## Examples

### [AWS S3](./aws-s3)

Shows simple steps in Python for hosting a static web site at S3.

Uses the [Python BOTO](https://aws.amazon.com/sdk-for-python/) library.


### [AWS Elastic Beanstalk](./aws-elastic-beanstalk)

Shows steps for deploying a web site to Elastic Beanstalk.

Uses the [AWS command-line interface](https://aws.amazon.com/documentation/cli/)
tools.


### [Vagrant](./vagrant)

Shows steps for deploying a web site to a VM using Vagrant.

Uses [Vagrant](https://www.vagrantup.com).


### [Vagrant w/Puppet](./vagrant-puppet)

Shows steps for using Puppet to deploy a web site inside a VM using Vagrant.

Uses [Vagrant](https://www.vagrantup.com) and various bits of [Puppet's]
(https://puppetlabs.com/puppet/puppet-open-source) open source components.
