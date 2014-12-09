
def safe_input()
    a = raw_input('anything')
    except (EOFError, KeyboardInterrupt): None
