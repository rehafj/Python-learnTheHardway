def add(a,b):
	print"adding %d and %d"%(a,b)
	x = a+b
	return x
def sub(a,b):
	print"sub %d and %d"%(a,b)
	return a-b
def div(a,b):
	print"deviding %d and %d"%(a,b)
	return a/b	
def multi(a,b):
	print"multplying %d and %d"%(a,b)
	return a*b
	
	
 # mown mehto dto define what he did below ( puzzle ) 
def d_(a,b,c,d):
	print" result from method"
	return a + (b-(c *(d / 2)))
print" lets do something with our funcitons"

age = add(30, 5) 
height = sub(78, 4)
weight = multi(90,2)
iq = div( 100, 2) 

print " age: %d , height %d, weoght %d, iq %d " %( age, height, weight, iq)

print" here is a puzzle" 
x=add(age, sub(height, multi (weight, div(iq,2))))
print x 
x = d_(age, height, weight, iq)
print x 


