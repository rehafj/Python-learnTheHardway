def c_a(cCount, bCount):
 print"yu have %d cheese" %cCount
 print"yo uhave %d boxes " %bCount
 print  """
  thats enough fot a party!
  get a blacnker 
  """
  
  
def a_m(*argv):
	ar1,ar2 = argv
	x = ar1*ar2
	print x
	



print" can wr give numbers direcyly>"
c_a(20,30)

print" or we can uase varibles form out script"
ac = 10 
ab = 20

c_a(ac,ab)

print" we can even do math inside it"
c_a(4+2,1+999)

print "and we can combine the two"
c_a(ac+10, ab-3)
x = int(raw_input('enter a number : '))
a_m(x,ab)
a_m(2,2)
a_m(2/2,1)
a_m(ac,ab)

