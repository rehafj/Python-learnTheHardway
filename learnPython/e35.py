from sys import exit 

run = [ "flee", "run ", "run away" ," escape", " aaaa" ]
head = [ " head" , "pain", " shoot" , " self" ]

def gold_room():
	print" this gold room is full of gold . how much do you take? "
	try:
		how_much = int(raw_input("->"))
	except ValueError:
		print" that is no nymber "
		dead("you did not enter a number you die!")
		exit(0)

		#if userinput.isdigit():
	if how_much < 50 :
		print" nice you are not greedy!"
		exit(0)
	elif  how_much >=50:
		dead( "you gready bastard!")
	else :
		print" type a number" 
	
	
	
	
def bear_room():
	print """ there is a bear here 
	the bear has a nunch of honey 
	the fat bear is infront of another door
	how are you going to move the door?"""
	bear_moved = False 
	
	while True: 
	# its a while so it can cuntine and ask ... expecting promps it will run across the statments again untill and input is givin - game loop 
	
	#if 1 ==1 :
		next = raw_input("> ")
		
		if "take " in next or " honey " in next:
			dead("the bear looks at you then slaps yout face off" )
		elif next == " taunt bear" and not bear_moved:
			print" the bear has moved from the door. you can pass now"
			bear_moved = True
		elif next == " taunt bear" and  bear_moved:
			print" the bear is mad and chews your leg off"
		elif next == " open door" and  bear_moved:
			gold_room()
		else: 
			print " i got no idea what that means" 
			
def cthulhu_room():
	print """ yu c the great evil holoho 
	he it whatever stares at you and yo go insane 
	do you flee for your life or eat you head?"""
	
	next = raw_input("> ")
	if next in run:
		start()
	elif next in head:
		dead("well that was weird")
	else :
		cthulhu_room()
	
	
def dead(expression):	
	print expression ,"  good job " 
	exit(0)

def start():
	print" you are in a dark room",
	print "take a door, left or right?"
	
	next = raw_input("> ")
	
	if next == "left" : 
		cthulhu_room()
	if next == "right" : 
		bear_room()
	else : 
		print " you stuumble alot and dinf you self questioning ..." 
		start()


#gold_room()
bear_room()
start()

	


