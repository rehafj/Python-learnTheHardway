the_count = [1,2,3,4,5]
fruits = ['apples', 'pranges', 'pears', 'appricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for loop  // number - item and fruit is accsessed within the list 
for number in the_count :
	print " the number is % d" % number + " as an array index  %r" %the_count[number-1] 
for fruit in fruits:
	print " a fruit of type : %s " % fruit 

for item in change :
	print " it can be done this way as well the item is %r " % item
	
# building an empty list

elements = [] 
# to go through a list of 5 items 
for i in range(0,6): 
	print " adding %d to the list " %i 
	# append is a function to add an eleletn to a list in python 
	if ( i < 5) :
		elements.append(i)
	else: 
		break
	
for i in elements:
	print " the element added is %d" %i 
	
tests = range(3,8)
for i in tests:
	print " the element added in test  is %d" %i 
	
tests.pop()
tests.pop()
tests.append(10)
for i in tests:
	print " after popping the elements are t  is %d" %i 
tests.reverse()
tests.insert(2, 100)
for i in tests:
	print " revercing the list  is %d" %i 
	
	
two_dimneiotnlalist = [['hi', 'hello'],['rehaf','nora']]
for i in two_dimneiotnlalist:
	print " revercing the list  is %r" %i 
	
