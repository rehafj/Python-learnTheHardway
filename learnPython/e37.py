import random  

print 1==1 and 1 !=1
mylist = [1,4,1]
print mylist
del mylist[1]
print mylist
del mylist 
try :
	print mylist 
except:
	print " error list delted"
num = 0
while ( num <  20) :
	num = num+ 1
	if num % 2 == 0 :
		print" repeating loop " 
		continue # will jump to the bgning of the loop while repeating / . 
		# breaks from the current loop 
		print" eill not print " 

	print num
print" break loop:" 

num = 0
while ( num <  20) :
	num = num+ 1
	if num % 2 == 0 :
		break
	print num, 
	
ls=[] 
ls2=[]
print " is ls the same as ls1 - empty stoewd in diffrentm emmory lcations even thoygh they are empty ",ls is ls2 
ls = "hi"
ls2 = "hi"

print " is ls the same as ls , th both have hi ", ls is ls
print  " \n what about arrays"

ls = ["hi"]
ls2 =["hi"]

print " is ls the same as ls , th both have hi ", ls is ls 

grades = ["a","b","c"]
if "F" not in grades:
	print" you pased"
else: 
	print " failed" 
	

#a = lambda x: 2 * 2 
#print a 

for i in (1, 2, 3, 4, 5):
   a =  lambda x: x * x
   print a(i),

print" escape char"
   


print "what \\ a does \a hahaha"
print "what \\ b does \b hahaha"
print "what \\ f does \f hahah"
print "what \\ v does \v hahah"
print" \x41"



#yeild example
class YesNoException(Exception):
   def __init__(self):
      print 'Invalid value'


answer = 'y'
answer = "yes"
if (answer != 'yes' and answer != 'no'):
   raise YesNoException
else:
   print 'Correct value'



exec("for i in [1, 2, 3, 4, 5]: print i,")

