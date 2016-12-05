from sys import argv

script, filename = argv

text = open(filename)

print" here is your file %r:" %filename
print text.read()

print"tye the file name again"
file_name = raw_input('fiel name: ')
# this is so cool! -a dded a write and read it will replace it 

txt_again = open(file_name , "w+")

print txt_again.read()
print txt_again.fileno()

new_info = raw_input('add things to add to file')
txt_again.write(new_info)
txt_again.close()


new_file = raw_input('enter a new file name')
opendFile = open(new_file ,"w+")
bla = raw_input('enter new text : ')
opendFile.write(bla)
opendfile.close()


#close()
#fileno()
#readline()
#write()
#after that add close()