from sys import argv
#imports from the sys oackdhe or ingine and imports the argv library or module 
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

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)

target.write("%r \n %r \n %r \n" %(line1, line2, line3) )
print" and finnay we clsoe it "

target.close()

new_file = raw_input('enter file name')
new_target = open(new_file, "w+")

text_inFile = raw_input('enter your text here: ')
new_target.write(text_inFile)
print"closing file"
new_target.close()
