#create file in /temp

file { '/temp/schoo;':
    ensure => file,
    owner  => 'www-data',
    group  => 'www-data',
    mode   => 0744,
}
