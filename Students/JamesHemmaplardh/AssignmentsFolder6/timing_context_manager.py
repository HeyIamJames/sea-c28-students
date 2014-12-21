"""Print elapsed time to run code."""

import time

class Timer:    
    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, *args):
        self.end = time.clock()
        print "elsapsed time(sec)", self.end - self.start

if __name__ == "__main__":
    with Timer() as t:
        for i in range(100000):
            i = i ** 20
