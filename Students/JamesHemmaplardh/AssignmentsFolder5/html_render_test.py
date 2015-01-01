from io import open, StringIO

import html_render as hr

reload(hr)

def render(page, filename):
    """
    render the tree of elements
    This uses cSstringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    page.render(f, u"    ")

    f.seek(0)

    print f.read()

    f.seek(0)
    open(filename, 'w', encoding="utf-8").write( f.read() )


page = hr.Html()

head = hr.Head()
head.append(hr.Title(u"This is a short story"))

page.append(head)

body = hr.Body()

body.append(hr.P(u"Once upon a time, something happened.",
              style=u"text-align: left; font-style: bold; color: blue"))


body.append(hr.P(u"The end.",
              style=u"text-align: center; font-style: bold; color: pink"))

page.append(body)

render(page, u"html_render_test_output.html")