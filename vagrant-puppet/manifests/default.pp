File {
  owner   => 'root',
  group   => 'root',
}

file { '/var/www':
  ensure  => directory,
  mode    => '0755',
}

file { '/var/www/vagrant':
  ensure  => directory,
  mode    => '0755',
  recurse => true,
  source  => '/vagrant/public',
}

class { 'nginx': }

nginx::resource::vhost { 'localhost':
  www_root => '/var/www/vagrant',
}
