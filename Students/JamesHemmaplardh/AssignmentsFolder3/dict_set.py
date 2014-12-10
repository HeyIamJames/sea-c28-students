"""This takes a dictionary, adds values, changes them and displays those chages."""

Dict = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}
print Dict
del Dict["cake"]
print Dict
Dict["fruit"] = "Mango"
print Dict.keys()
print Dict.values()
print "cake" in Dict
print "Mango" in Dict
print "Mango" in Dict.values()

Dict2 = range(16)
Dict3 = []
for i in Dict2:
    Dict3.append(hex(i))
Dict4 = dict(zip(Dict2, Dict3))
print Dict4

Dict5 = {}
for key, val in Dict.items():
	Dict5[key] = val.count('a')
print Dict5

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
	if not i % 2:
		s2.add(i)
	if not i % 3:
		s3.add(i)
	if not i % $:
		s4.add(i)

print s2
print s3
print s4

print s3.issubset(s2)
print s4.issubset(s2)

Set1 = set("Python")
Set1.add('i')
print Set1

Set2 = frozenset("marathon")
print Set1.Union(Set2)
print Set1.intersection(Set2)

