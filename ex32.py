

######## Loops and Lists ###########


the_count = [1, 2, 3, 4, 5, ]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#####  This first kind of for -loop goes through a list

for number in the_count:
    print "this is the count %d" % number


######### same as above

for fruit in fruits:
    print "A friut of type: %s" % fruit


##### Also we can go through mixed lists too
#### we have to use %r since we dont know what in it

for i in change:
    print "I got %r" % i


#### We can also build lists #####  First start with an empty one

elements = []


#### Then use a range of functions to do 0 to 5 counts

for i in range (0, 6):
    print "Adding %d to the list." % i
    #### append is a function that lists understand
    elements.append(i)



##### Now we can print them out tooo

for i in elements:
    print "Element was: %d" % i
