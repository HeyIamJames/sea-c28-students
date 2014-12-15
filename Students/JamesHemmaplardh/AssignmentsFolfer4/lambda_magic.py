#make a function to return a list of functions 

x = [(lambda arg: (lambda x: arg + x))(i) for i in range(11)]

#if __name__ == "__main__":