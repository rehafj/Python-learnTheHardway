import random 
import time

rock = 1 
paper = 2 
sizors = 3

names = { rock: "rock", paper: "paper", sizors:"scissors"}
rules = { rock: sizors, paper: rock, sizors: paper}

player_score = 0
comp_score = 0

def start():
	while game():
		pass
	scores()
	

def game():
	player = move()
	computer = random.randint(1,3)
	result( player, computer)
	return playagain()

def move():
	while True: 
		print
		player = raw_input("enter 1 for rock 2 for paper and 3 for sizors")
		try:
			player = int(player)
			if player in (1,2,3):
				return player
		except ValueError :
			pass 
		print " ops please enter 1 or 2 or 3 "

def result ( player, comp) :
	print "1..."
	time.sleep(1)
	print "2..."
	time.sleep(1)
	print "3..."
	time.sleep(1)
	
	print" comp chose {0} !".format(names[comp])
	global 	player_score , comp_score 
	if player == comp: 
		print " its a tie!"
	else: 
		if rules[player]==comp:
			print" player wins"
			player_score+=1
		else:
			print" comp wins"
			comp_score+=1
def 
			