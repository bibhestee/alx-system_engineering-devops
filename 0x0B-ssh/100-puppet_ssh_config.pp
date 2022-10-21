# configure a SSH client configuration using puppet

exec {'Sed':
  command => 'sudo sed -i 's/^#   PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/ssh_config,
}

exec {'sed':
  command => 'sudo sed -i 's/^#   IdentityFile ~\/.ssh\/id_rsa /IdentityFile ~\/.ssh\/school/g' /etc/ssh/ssh_config,
}
