# use Puppet to make changes to coniguration file
include stdlib

file_line { 'Turn off passwd auth':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '    IdentifyFile ~/.ssh/school',
  replace =>  true,
}
