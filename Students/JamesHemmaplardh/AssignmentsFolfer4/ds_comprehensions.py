food_prefs = {u"name": u"Cris",
              u"city": u"Seattle",
              u"cake": u"lemon",
              u"fruit": u"pomegranate",
              u"salad": u"chop",
              u"pasta": u"lasagna"}
print('{name} is from {city}, his favorite cake is {cake}cake with a side of {fruit} and {salad}, then {name} finishes it off with a zesty {pasta}!'.format(**food_prefs))

s1 = dict([(x, hex(x)) for x in (range(16))]) 

food_prefs2 = dict(food_prefs)
for key, val in food_prefs2.items():
      food_prefs2[key] = val.count(u'a')

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if i % 2 == False:
        s2.add(i)
	if i % 3 == False:
		s3.add(i)
	if i % 4 == False:
		s4.add(i)



