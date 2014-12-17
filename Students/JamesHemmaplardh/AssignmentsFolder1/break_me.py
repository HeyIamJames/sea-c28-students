# this is a name error
x = broken()

#this is a type error 
x = ("james",) + "hemmaplardh"

#this is a SyntaxError
x = ("james",)  "hemmaplardh

#this is an AttributeError
class james(object):
    pass

o = james()
print o.james