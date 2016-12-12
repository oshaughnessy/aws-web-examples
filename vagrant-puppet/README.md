# Running a web site in a virtual machine using Vagrant... via Puppet

This example shows how to use Puppet to install a web server and site content
into a virtual machine run by [Vagrant](https://www.vagrantup.com).

What does it do?

* It runs an Ubuntu 16.04 virtual machine.
* It installs the Puppet agent.
* It installs a handful of module dependencies from the
  [Puppet Forge](https://forge.puppet.com).
* It invokes the Puppet agent to install nginx, configure a virtual host,
  and copy the files from the "public" subdirectory to a local directory
  in the VM.
* It tries to query Nginx and show you the resulting HTML as a visual
  test that the site is working.

Assumptions:

* You have Vagrant installed on your computer.
* Your have a compatible [virtualization provider](https://www.vagrantup.com/docs/getting-started/providers.html) installed, like VirtualBox or VMWare Fusion.
* You have a decent network connection, which may be used to download the
  Ubuntu Vagrant image and will definitely be used to download OS updates and
  Puppet modules.

To try it, run `vagrant up` from this directory.

When you're done, run `vagrant destroy`.
