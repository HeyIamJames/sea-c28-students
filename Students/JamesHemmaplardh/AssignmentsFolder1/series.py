def fibonacci(n):
    """this function adds the two previous values in the fibonacci series"""
    if n < 0:
        return None
    if n == 0:
        return 0
    elif n == 1:
    	return 1
    else:
    	return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    """this function adds the two previous values in the Lucas series"""
    if n < 0:
    	return None
    elif n == 0:
        return 2
    elif n == 1:
    	return 1
    else:
    	return lucas(n-1)+lucas(n-2)

def sum_series(a, b=0, c=1):
    """this function adds the previous two values, the b and c paramaters determine the first 2 numbers in the sum series"""
    if a < 0:
    	return None
    elif a == 0:
    	return b
    elif a == 1:
        return c 
    else:
        return sum_series(a-1, b, c) + sum_series(a-2, b, c)

assert (fibonacci >=0, lucas >= 0, sum_series >= 0), "n, a, b and c are positive integers"
# the assert statment ensures that the functions above use only arguments that are positve integers 