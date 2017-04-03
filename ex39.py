###### Dictionary example #######


# create a mapping of state to abbreviation

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

### Create a basic list of states and some cities in them

cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }


# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print some cities


print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states

print '-' * 10
print "Michigan abbv is : ", states['Michigan']
print "florids abbv is: ", states['Florida']



# do it by using the state then cities dict

print '-' * 10
print "michigan has : ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]



#### print every state abbv
print '-' * 10
for state, abbrev  in states.items():
    print "%s is abbreviated as %s" % (state, abbrev)



# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev,city)


# now do both at the same time

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated as %s and has city %s" % (state, abbrev, cities[abbrev])


print '-' * 10
# safely get a abbreviation by state that night not be there

state = states.get('Texas')


if not state:
    print "SOrry not Texas"


## get a city with default value

city = cities.get('TX', 'Does not exits')
print "the city for the state 'TX' is %s" % city
