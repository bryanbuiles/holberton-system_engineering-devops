# Using Puppet, kills process killmenow
exec { 'pkill killmenow':
path => ['/usr/bin']
}
