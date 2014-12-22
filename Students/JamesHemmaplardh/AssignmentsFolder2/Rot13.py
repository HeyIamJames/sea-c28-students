def rot13(a):
    a = a.encode("rot13")
    return a
    

if __name__ == "__main__":
	assert rot13(u"i am batman") == u"v nz ongzna"
	print " rot13 demo: 'i am batman' = 'v nz ongzna' "
