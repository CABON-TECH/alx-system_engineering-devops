# Using puppet to change SSH config file
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/school\n   PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
