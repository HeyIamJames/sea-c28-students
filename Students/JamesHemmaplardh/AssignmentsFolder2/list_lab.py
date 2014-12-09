#!/usr/bin/env python
# add that line later

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
for p in Fruits[0:]:
    if p == "P": #this may be wrong
        print 
    else:
        print "There are no fruits that start with 'P'"

print Fruits
Fruits.pop()
print Fruits
RemoveFruit = raw_input('What fruit do you hate?')
Fruits.remove(RemoveFruit)
print Fruits
for x in Fruits:
    RateFruit = raw_input('Do you like fruit ') 
    if RateFruit in Fruits:
    	Fruits.remove(RateFruit)
    else:
    	print RateFruit, "not a valid input, type yes or no"
print Fruits


#'hi'[::-1] = 'ih'
for i in reversed(NewFruits):
	print i
Fruits.pop()
print Fruits
print NewFruits

