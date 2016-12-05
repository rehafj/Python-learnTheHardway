print" you enter a room with two doors, do you go thrhough door 1 or door 2 ? " 
door = int(raw_input('->'))
if door == 1 : 
	print" there is a gaint bear, what do you do ?"
	print " 1 ; take the cake " 
	print " 2 : scream at the bear" 

	bear = int(raw_input('->'))

	if bear == 1: 
		print" the bear eats your face off, good job" 
	elif bear == 2: 
		print " the bear east s your leg off" 
	else : 
		print " well doing %s is better! the bear runs away " % bear
		
elif door == 2: 
	print" ABYSS UPI stare at it "
	print " 1 ; bluebarries " 
	print " 2 : yellow jacket "
	print " 3: revolvers yelling melodies"
	
	bear = int( raw_input('->'))
	
	if bear == 1 or bear == 2 : 
		print" ypur bpdy survives a mind of jelly " 
	else : 
		print " teh insaanty drives you home" 

else :
	print " you stubmple and fall"
	
	 

		