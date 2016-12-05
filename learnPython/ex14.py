from sys import argv 

script, username, sistersname = argv
prm = '->'

print "hi %s this is the %s script ." %(username, script)
print "i would like to ask you a few questions"
print" do you like me %s" %username
print" do you like me", username
like_me = raw_input(prm)

print "where do you live ",username
live = raw_input(prm)

print"what type of computer do you have"
comp = raw_input(prm)

print"""
alright %s, i didnt forget your sister %r her name is cool 
you said its %r about liking me
you live in %r
and you have a comp of type %s"""%(
username, sistersname, like_me, live, comp)

