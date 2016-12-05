# MODULES - lists and varibles 
from sys import exit 
hp = 0 
attacks = ["attack" , "sword", "Shiled"]
flee = ["run", "flee", "escape"]
prompt = '->'


	
def main_room():

	print name, ": where am i - it looks liek its a damp path up a head \n looks like the path leads left and right"

	next = raw_input(prompt)
	
	if next == "right" :
		gaurds()
	elif next == "left":
		room()
	else :
		main_room()
		

def room():
	print""" you enter a room filled with items...
	you put on some armor 
	your armor goes up 
	"""
	global hp
	hp = hp +100
	
	print" your armor value is %d" %hp 
	
	next = raw_input(prompt)
	
	if next == "right" :
		gaurds()
	elif next == "strait":
		main_path()
	else :
		print" you failt o comprehend what you typed and choose to go ahead instead of listing to jabber"
		main_path()
		

def gaurds():
	print""" i hope you have armor equipped! 
	a gaurd charges!
	"""
	if hp > 0:
		print" you charge at the gaurd with your armor and knock him out"
	else : 
		print " the gaurd hits you and you are doomed! "
		dead(" dreaded gaurd")
	
	print" you think of what path to take now that the gaurd has been dealth with!"
	
	next = raw_input(prompt)
	
	if next == "right" :
		outside()
	elif next == "strait":
		main_path()
	else :
		main_path()
		
def dead(reason):		
	print " you died by the hands of ", reason
	exit(0)

def main_path():
	print" follwing the main path you c a chiny room you find armor and equip it! "
	global hp 
	hp = hp + 50
	print" your armor value is %d !" %hp 
	print " yu encounter a boss ! " 
	
	if hp > 100 :
		print " with all the items you found  this loked like an easy battle"
	else :
		print " this will be tough"

	print " what will you do ?" 
	next = raw_input(prompt)
	
	if next in attacks: 
		print"you attack the monsyer"
		win()
	elif next in flee:
		print " you flee! towards the door and headoutside  \n you  run  "
		outside()
	else : 
		dead("monster")

def outside():
	print" you manage to escape! yay"
	exit(0)
def win():
	print " you won the game!"
	exit(0)

print"""  hi there ! please fill put this information befre mocing on 
remind me - who are you again? 
"""
name = raw_input(prompt)
print """ ok %s ! \n * pUNCH* you black out 
you find your self in a doungon""" % name
main_room()