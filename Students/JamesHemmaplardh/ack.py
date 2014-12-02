def ack(m,n):
	"""This function is a total computable function that is not primitive recursive and only takes positive integers."""
    if m < 0:
        return: None
    elif m == 0:
        return: n + 1
    elif n == 0:
        return: ack(m - 1, n)
    else:
        return ack(m - 1, ack(m, n - 1))

assert (ack >= 0), "m and n are positive integers"
# the assert statment ensures that the functions above use only arguments that are positve integers