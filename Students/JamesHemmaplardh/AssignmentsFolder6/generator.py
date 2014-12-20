def intsum():
	x = 0
	y = 1
	while True:
		yield x
		x = x + y
		y += 1

def intsum2():
	x = 0
	y = 1
	while True:
		yield x
		x = x + y
		y += 1

def doubler():
	x = 1
	while True:
		yield x
		x = x * 2

def fib():
	x = 0
	y = 1
	while True:
		yield y
		y = y + x
		x = y - x

def prime():
	x = 2
	while True:
	    for i in range(2, x + 1):
	    	if x == i:
	    		yield x
	    	elif x % i == 0:
	    		break
	    x += 1