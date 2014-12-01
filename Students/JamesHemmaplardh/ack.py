def ack2(M, N):
	"""This function is a total computable function that is not primitive recursive and only takes positive integers."""
    if M <= 0:
    	return None
    elif M == 0:
        return N + 1
    elif N == 0:
        return ack1(M - 1, 1)
    else:
        return ack1(M - 1, ack1(M, N - 1))