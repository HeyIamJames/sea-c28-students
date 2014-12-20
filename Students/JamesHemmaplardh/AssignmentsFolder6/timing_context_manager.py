"""Print elapsed time to run code."""
import time

def foo():
 	for i in range(100000):
 		i = i ** 20

if __name__ == "__main__":
	start = time.time()
	foo()
	end = time.time()
	print "elapsted time(sec)", end - start 

