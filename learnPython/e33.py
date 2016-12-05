import random 

numbers = [] 

	
def gen ( x, y, z ) :
	i=0
	" this is a gen number pass it a value it will append it into an array, " 
	while i< x:
		print " at the top i is %d " %i 
		f = random.randint(y,z)
		print" ranom number f  is " , f
		numbers.append(f)
	
		i += 1
		print" numbers now " , numbers 
		print " at the end of the loop / buttp, i is %d " %i
	print" exiting loop at i = ", i 
	
	
def loopfor ( y, z ) :
	for d in range(y,z):
 
		f = random.randint(y,z)
		print" ranom number f  is " , f
		numbers.append(f)
		print" numbers now " , numbers 
	
	
"""	
#while i<6:
	#print " at the top i is %d " %i 
	#x = random.randint(0,9)
	#print" x is " , x
	#numbers.append(x)
	
	i += 1
	print" numbers now " , numbers 
	print " at the end of the loop / buttp, i is %d " %i
	"""
	
	
size = int(raw_input('size : '))
range1 = int(raw_input('begning random number '))
range2 = int(raw_input('last random number '))
range2= range2+ 1

gen(size, range1, range2)

print" prinintg all the numbers "
for i in numbers: 
	print i
loopfor(range1, range2)
for i in numbers: 
	print i

