
def safe_input():
    a = raw_input('anything')
    try: 
    except(EOFError, KeyboardInterrupt): 
    	return None
