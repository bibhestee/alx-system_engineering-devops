# This is a puppet script that configures a brand new Ubuntu machine
#   Requirement:
#       The name of the custom HTTP header must be X-Served-By
#       The value of the custom HTTP header must be the hostname of the server Nginx is running on
# Update apt package
exec {'apt-update':
  command => '/usr/bin/apt-get update'
}

# Install nginx package
package {'nginx':
  require => Exec['apt-update'],
  ensure  => installed,
}

# Modify nginx configuration for custom HTTP header

$header = "\\\n\t\tadd_header X-Served-By $hostname;"

exec {'nginx_config':
  user    => root,
  command => "/usr/bin/sed -i '51i ${header}' /etc/nginx/sites-available/default",
}

# Restart Nginx server
exec {'nginx_restart':
  user    => root,
  command => '/sbin/service nginx start',
}
