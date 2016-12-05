#using the system namespace and we used argv module 
from sys import argv 
#varibles got from user at the begning ( Argv) and assigned to script and input_file 
script, input_file = argv
#passes a file object and reads the dara 
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
#prints a single line 	
def print_a_line(line_Count, f):
	#f.seek(0) understood if seek is 0 it will always print at byte 0 cz it reads and resets it to line 1!!! 
	print line_Count, f.readline()# , if the comma is added it wont have a new line !
	 # the head will move down - its because we did not reset it if we added a seek here( uncomment below and uu will see)
# assigning the object file ad adding the input file 	
target = open(input_file)
#calling prints 
print"lets print the whole file"
print_all(target)


print" lets rewind"
rewind(target)
#returns to ht e head of the file using seek 
#VI DO NOT FORGET 
#VI DO NOT FORGET 
#VI DO NOT FORGET 

#VI DO NOT FORGET 

print_a_line(1, target) # thihes fixses it 1!!!!!!! - so read lne saves it tand moves to the next ien VI DO NOT FORGET 

print" lets print three lines"
#assigning 
c_l = 0
# do it three times 
while( c_l < 3):
	#c_l = c_l+1
	c_l+= 1
	print_a_line(c_l, target)	 #calls the method 
	
print" pout of loop"
	
	
	#check and ask - 