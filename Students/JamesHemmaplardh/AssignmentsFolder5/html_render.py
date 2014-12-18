#!/usr/bin/env python

class Element(object):
    tag = u'This is a tag'
    indent = u"    "

    def __init__(self, content= None, **kwargs):
        if content == None:
            self.content = []
        else:
            self.content = [content]
        
        self.attributes = kwargs

    def append(self, element):
    	self.content.append(element)

class Html(Element):
	tag = u"html"

class Head(Element):
	tag = u"head"

class Body(Element):
	tag = u"body"

class P(Element):
	tag = u"p"

class SelfClosingTag(Element):
	def render(self, file_out, ind = "    "):
		file_out.write('{}<{}{} />\n'.format(ind, sef.tag, self.attributes))

class A(SelfClosingTag):
    tag = u"a"
    def __init__(self, link, content):
        OneLineTag.__init__(self, content, href=link)

class UI(Element):
	tag = u"ul"

class LI(Element):
	tag = u"li"

