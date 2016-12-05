formatter = "%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %("one", "two", "three", "four")
print formatter %( True, False, True, False)
print formatter % ( formatter,formatter,formatter,formatter)
print formatter % (
"i have this thing/n",
"it is called a string " , 
" but i did nothingmor text text text text text  ", 
"so good night")


x = "one " 
y="two"

print x + y
print x , y
print x
print y

print x,
print y

print formatter