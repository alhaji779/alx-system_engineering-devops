# holberton user and open a file without any error message.

exec {'OS security hard config':
  command => 'sed -i "/^holberton hard/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}


exec {'OS security soft config':
  command => 'sed -i "/^holberton soft/s/5/40000/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
