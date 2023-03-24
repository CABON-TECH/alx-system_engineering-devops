# A Puppet manifest that kills a process named 'killmenow'

exec { 'kill_process':
  command  => '/usr/bin/pkill killmenow',
  onlyif   => '/usr/bin/pgrep killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
