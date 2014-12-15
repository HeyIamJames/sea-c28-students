x = [(lambda arg: (lambda x: arg + x))(i) for i in range(11)]
"""Increment list value of [] by ().""" 

if __name__ == "__main__":
    print "test: x[2](1) ==", 3