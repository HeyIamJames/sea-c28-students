"""Print elapsed time to run code."""
import time

def foo():
 	for i in range(100000):
 		i = i ** 20


start = time.time()
#def foo()
end = time.time()
print end - start




