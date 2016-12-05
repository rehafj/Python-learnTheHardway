""" to import evrything just ty[e  from  e25 ( file name) import * now you can use the funcitons directly without an instance of the file each time"""

def break_words(stuff):
	"""this funciton will break workds for us"""
	#words = stuff.split(' ') 
	#words = stuff.split('>>') 
	words = stuff.split(" ") 
#stuff is sent in as an array or strings in this case 
# returns words spilit up ( array of littitals ) 

	return words 

	
def sort_words(words):
# this is so fing cool ! i mean it shows up as help never knew this so cool :D 
# these are called documintaion comments 
	"""sort the words""" 
	#sorted is a method that rearabges the list based on asc values probably  - asc values ? 
	# sorted can be used on ints as well 
	return sorted(words)

def print_first_word(words):
	"""print the first word after popping it off """
	word = words.pop(0)
	print word

def print_last_word(words):
	""" print the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentences(sentence):
	""" takes in a full sentence and returns the sorted word """
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	""" stores the word  then prints then print the first and last one """
	words = sort_sentences(sentence)
	print_first_word(words)
	print_last_word(words)
	
	
	
	