ten_things = "apples oranhes crows telephone light sugar"

print" no 10 items in the list! add more" 
stuff = ten_things.split(' ')
ten = stuff
print stuff,"\n"
more_stuff = ["day","night", "song", "frisbie" ,"corn", "banna", "girl" ,"boy"]
while len(stuff) !=10 :
	next_one = more_stuff.pop()# 0 for initial list elements
	print " adding ", next_one 
	stuff.append(next_one)
	print" the list holds %d items now" %len(stuff)

print" there we go ! ", stuff 

print  " lets fo something witht hese stuff"
print stuff[1]
print stuff[-1]
print stuff.pop()
print stuff
i = 0 
for item in stuff:
	print item
	i = i + 1
	var = str(i)
	print var,
print var.join(stuff) # ptinys all 9 

i= 0 
while i < len(stuff):
	
	var = i
	stuff[i] = str(i) + " " + stuff[i]
	i += 1
print stuff	
print '*'.join(stuff)
print '#' .join(stuff[3:5])

	