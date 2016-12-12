# Running a web site in a virtual machine using Vagrant

This example shows how to install a web server and site content
in a virtual machine using [Vagrant](https://www.vagrantup.com).

What does it do?

* It runs an Ubuntu 14.04 virtual machine.
* It installs Nginx.
* It links the local "public" subdirectory to the Nginx document root
  within the VM, so that the VM's web server is serving up those files.
* It tries to query Nginx and show you the resulting HTML as a visual
  test that the site is working.

Assumptions:

* You have Vagrant installed on your computer.
* Your have a compatible [virtualization provider](https://www.vagrantup.com/docs/getting-started/providers.html) installed, like VirtualBox or VMWare Fusion.

To try it, run `vagrant up` from this directory.

When you're done, run `vagrant destroy`.
