from sys import argv

script, filename = argv

print "we are going to erase %r" %filename
print "if you dont want that hit cnrtl-c"
print" if you want that hit return"

raw_input('?')
print"opening the file"
target = open(filename, "w")

print" turnicating the file, good by!"
target.truncate()

print"now i am going to ask you for three lines"
line1= raw_input('enter line one data:')
line2 = raw_input('enter line2:')
line3 = raw_input('line 3:')

print" i am going to write these to file"

target.write(line1)
target.wrote("\n")
