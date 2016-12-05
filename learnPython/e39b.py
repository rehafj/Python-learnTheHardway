states = {
	'oregon':'OR',
	'florida':'FL',
	'Californa':'CA',
	'newYork':'NY',
	'michigan':'MI'


}

cities = {
	'CA': 'sanfransisico',
	'MI':'destroit',
	'FL':'Jacksonvill'
	}
	
# add some more cities 

cities['OR'] = 'portalnd'
cities['NY'] = 'newyourl'

print ' ---0--- '* 5
print "ny has the the city ", cities['NY']
print "OR has the the city ", cities['OR']


print ' ---0--- '* 5
print "michigan has the abv", states['michigan']
print "florida has the abv", states['florida']

print ' ---0--- '* 5
print " the city in ny is ", cities[states['newYork']]
print " the city in florida is ", cities[states['florida']]
print ' ---0--- '* 5

# key one and value one ...etc 
for state, abbrev in states.items():
	print "%s state is abbrvited %s " % (state, abbrev) 

print ' ---0--- '* 5
for state, abbrev in cities.items():
	print "%s state has a capital  %s " % (state, abbrev) 
print ' ---0--- '* 5

for state, abbrev in states.items():
	print "%s state is abbrvited %s and has a city %s"%( state, abbrev, cities[abbrev])
	
print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


#check collections. ordered ditionaries 