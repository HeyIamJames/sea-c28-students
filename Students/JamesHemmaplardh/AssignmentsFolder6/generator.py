def sum_of_integers():
	x = 0
	y = 1
	while True:
		yield sum_of_integers
		x += 1
		sum_of_integers += x 

def doubler():
	x = 1
	while True:
		yield x
		x = x * 2