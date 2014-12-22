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

if __name__ == "__main__":
    x = 5
    assert lucas(x) == 11
    x = 7 
    assert fibonacci(x) == 13
    x = 3
    y = 4
    z = 3
    assert sum_series(x, y, x) == 10
    print "fibonacci, lucan adn sum_series functions are working."
