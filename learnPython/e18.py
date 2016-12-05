#similr to scriptwitharg vale 

def print_two(*args):
	arg1, arg2 = args
	print "arg1:%r, arg2: %r" %(arg1, arg2)
 
def print_two_again( arg1, arg2):
	print"arg1 is % r, arg 2 is %r"%(arg1, arg2)

def print_one(arg1):
	print" arg1", arg1
	
def print_():
	print" i got nothin!"
	
print_two('rehaf' , 'shadin')
print_two_again(5,10)
print_one("haha")
print_()
