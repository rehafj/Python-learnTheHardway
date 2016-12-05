from sys import argv 

script, first, second, third = argv

print " the script is called", script 
print" your first var is ", first
print " your second var is called", second
print third 

third = raw_input('enter third again')

print '''
the script is %r 
the first var is %r
secod is %r 
and thirs is now %r
'''%( script, first, second, third)
