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

    def render(self, file_out, ind = u"    "):
        attributes = ''
        for (key, value) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = key, value = value))
        file_out.write(u'\n%s<%s%s>\n' % (ind, self.tag, attributes))
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent + ind)
                file_out.write(item)
        file_out.write(u'\n%s</%s>' % (ind, self.tag))

class OneLineTag(Element):
    def render(self, file_out, ind = u"    "):
        attributes = '  '
        for (key,value) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = key, value = value))
        file_out.write(u'\n%s<%s%s>\n' % (ind, self.tag, attributes))
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent + ind)
                file_out.write(unicode(item))
        file_out.write(u'\n%s</%s>' % (ind, self.tag))

class Html(Element):
    tag = u"html"

    def render(self, file_out, ind=u""):
        print u"hmtl"
        file_out.write(u"<!DOCTYPE html>")
        Element.render(self, file_out)


class Head(Element):
    tag = u"head"


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"

class SelfClosingTag(Element):
    def __init__(self, **attributes):
        self.attributes = attributes

    def render(self, file_out, ind = u"    "):
        attributes = ''
        for (key,value) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = key, value = value))
        file_out.write(u'\n%s<%s%s>\n' % (ind, self.tag, attributes))


class Hr(SelfClosingTag):
    tag = u"hr"


class Title(OneLineTag):
    tag = u"title"


class A(OneLineTag):
    tag = u"a"
    def __init__(self, link, content):
        OneLineTag.__init__(self, content, href=link)


class H(OneLineTag):
    def __init__(self, level, content, **attributes):
        OneLineTag.__init__(self, content, **attributes)

        self.tag = u"h%i"%level

class Ul(Element):
    tag = u"ul"


class Li(Element):
    tag = u"li"

class Meta(SelfClosingTag):
    tag = u"meta"
