
while True:
    '''Return 'None' when EOFE or KeyboardInterrupt is executed'''
    try:
        x = raw_input("enter text")
        break
    except (EOFError, KeyboardInterrupt):  
        print "'None'"

'''
while True:
    try:
        x = raw_input("enter text")
        break
    except (EOFError, KeyboardInterrupt):  
        return None
'''
