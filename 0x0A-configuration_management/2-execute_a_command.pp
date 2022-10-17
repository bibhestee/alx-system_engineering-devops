# Kill a process named 'killmenow' using puppet

exec {'pkill':
  command => '/usr/bin/pkill -f killmenow',
}
