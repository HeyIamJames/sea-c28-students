class Element(list):
	opening_tag = "<>"
	closing_tag = "</>"
	def render(self):
		all_out = [self.opening_tag] + self + [self.closing_tag]


#		output = "<>\n"
#		output += self[0]
#		output += "\n</>"
		print all_out

"""
def __init__(self):
	self.contents = []
