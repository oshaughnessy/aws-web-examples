# S3

This example shows how to host a simple static web site at AWS using S3.

What does it do?

* It creates a new S3 bucket with the web hosting feature enabled.
* It copies the files from the "public" subdirectory to the bucket.
* It gives you back the URL to the new site.
* It verifies that it's accessible over HTTP.

There are more sophisticated ways to host a web site in S3. This just
shows a simple way to do it using Python.
