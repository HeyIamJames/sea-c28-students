def rot13():
    a = raw_input('Enter Code:')
    return a.encode("rot13")
    

if __name__ == "__main__":
	assert rot13(u"I am, BaTman   ") == u"V nz, OnGzna   "
	print " rot13 demo: 'I am, BaTman   ' = 'V nz, OnGzna'     "
