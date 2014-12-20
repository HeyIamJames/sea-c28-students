def wrapper_decorator(func):
	def wrapper(*args, **kwargs):
	    return u"<p>" + func(*args, **wkargs) + u"</p>"
	return wrapper 

