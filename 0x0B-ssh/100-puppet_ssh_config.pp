# configure a SSH client configuration using puppet

exec {'Host':
  command => 'Host 100.26.225.121\nPasswordAuthentication no\nIdentityFile ~/.ssh/school',
}
