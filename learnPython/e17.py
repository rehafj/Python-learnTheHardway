from sys import argv 
from os.path import exists

script, from_file, to_file = argv

print" copying file from %s to %s " %(from_file, to_file)

#e could do these two in onel line how ? 
#indata = infile.read(open(from_file)


#this could be done in oneline 
infile = open(from_file)
data = infile.read()


testinfile = open(from_file).read() #no need to close this after 
#x = file object 
# y = x.read

print"the input file is %d long" %len(data)

print"dows the output file exsist? %r" % exists(to_file)
print" return to cont"
raw_input('->')


outfile= open(to_file, "w+")
outfile.write(data)

print" all done"
outfile.close()
infile.close()
