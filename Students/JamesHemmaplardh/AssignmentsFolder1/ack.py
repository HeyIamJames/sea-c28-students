"""This function is a total computable function that is not primitive recursive and only takes positive integers."""
def ack(m,n):
    if m < 0:
        return None
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, n)
    else:
        return ack(m - 1, ack(m, n - 1))

if __name__ == "__main__":
	m = 3
	n = 5
	assert ack(m, n) == 6
	print "Ackermans function is working."

