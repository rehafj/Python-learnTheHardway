print "lets practice evrything"
print" you \' need to know \' about escape with \\ like \n new lines  and  \t tabs"

poem = """
\t the lovly world 
with logic so fimly planter 
cannot dissern \n the need for love 
nor comprehend passion from intuition 
and requires an explanation  
\n\t\twhere there is none
"""
#prints the var 
print "_"*10
print poem 
print "_" * 10 

five = 10 -2 + 3 - 6
print " this should be five %d" % five 
#method or functipons with returning varibles assigned 
def secret_forumal( started) :
	jellyB = started * 500 
	jars = jellyB / 1000
	creats = jars / 100 
	return jellyB, jars, creats
#assigning values to the methof above 
start_point = 10000 
beans,  jars , creates = secret_forumal( start_point)

print " with a starting point of : %d " %start_point
print " we have %d, beans and %d jars and finnaly %d creates! " %(beans,  jars , creates)

# assignin gthe varible to the varibles from itself / 10 
start_point = start_point /10 

print " we ca nalso do it this way " 
# print stattment maps value to returned valyues from method directly 
print " we have %d beans , %d jars , and %d creates " % secret_forumal( start_point) 