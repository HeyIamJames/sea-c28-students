#!/usr/bin/env python
# add that line later


"""This program modifies a list based on a users input."""

Fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print Fruits
NewFruit = raw_input('Enter your favorite fruit:')
Fruits.append(NewFruit)
print '\n'.join(Fruits)
NewNumber = int(raw_input('Enter the number of the fruit on the list you wish to see, descending from top:'))
print Fruits[(NewNumber - 1)]
Fruits = Fruits + ["Pineapple"]
Fruits.reverse()
print Fruits
Fruits.insert(0, "Lychee")
print Fruits
for p in Fruits:
    if p[0] == "P": #this may be wrong
        print p
    else:
       print "There are no fruits that start with 'P'"

print Fruits
Fruits.pop()
print Fruits
RemoveFruit = raw_input('What fruit do you hate?')
Fruits.remove(RemoveFruit)
print Fruits
for x in Fruits:
    RateFruit = raw_input('yes/no, Do you like fruit %s ' %x)
    if RateFruit == "no":
        Fruits.remove(x) 
    if RateFruit == "yes":
    	pass
    else:
    	print RateFruit, "not a valid input, type yes or no"
print Fruits


#'hi'[::-1] = 'ih'
NewFruits = []
for i in Fruits:
	NewFruits.append(i[::-1])
Fruits.pop()
print Fruits
print NewFruits

