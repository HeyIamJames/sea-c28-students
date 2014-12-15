food_prefs = {u"name": u"Cris",
              u"city": u"Seattle",
              u"cake": u"lemon",
              u"fruit": u"pomegranate",
              u"salad": u"chop",
              u"pasta": u"lasagna"}
print('{name} is from {city}, his favorite cake is {cake}cake with a side of {fruit} and {salad}, then {name} finishes it off with a zesty {pasta}!'.format(**food_prefs))

Dict1 = range(16)
Dict2 = []
for i in Dict1:
	Dict2.append(hex(i))
Dict3 = dict(zip(Dict1, Dict2))

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



