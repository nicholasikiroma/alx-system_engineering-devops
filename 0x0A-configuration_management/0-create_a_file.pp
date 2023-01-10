# Creates a file in /tmp

$str = 'I love Puppet'

file { '/tmp/school':
  ensure  => file,
  content => $str,
  mode    => '0744',
  owner   => www-data,
  group   => www-data
}
