#!/usr/bin/env python

class Element(object):
    tag = u'This is a tag'
    indent = u"    "

    def __init__(self, content= None, **kwargs):
        if content == None:
            self.content = []
        else:
            self.content = []
        
        self.attributes = kwargs

    def append(self, element):
    	self.content,append(element)

class Html(Element):
	tag = u"html"

class Head(Element):
	tag = u"head"

class P(Element):
	tag = u"p"