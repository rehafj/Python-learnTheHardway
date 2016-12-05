people = 30 
cars = 20 
bus = 15 
a = 10 

if cars > people :
	print " we should take the cars"
elif cars < people: 
	print" we shoudl not take the cars"
	
# it will not go here if the ones above it are ture 	or one is true if it is a n if it will check it regardles and else if will not 
elif a < cars :
	print " anther true " 
	
else :
	print" we can't decide "
	
	
if bus > cars : 
	print" too many busses" 
elif bus < cars:
	print " maybe we could take the buss" 
else: 
	print" we still can't decide "
	
if people > bus : 
	print " lets just take the buss"
else: 
	print " Fine lets stay home then !"