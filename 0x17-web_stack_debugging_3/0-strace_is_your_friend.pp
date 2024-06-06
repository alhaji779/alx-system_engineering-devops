# fixes a file
exec {'replaces wrong phpp in file':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /var/www/html/wp-settings.php'
}
