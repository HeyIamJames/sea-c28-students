def make_incrementor (n): return lambda x: x + n

foo = range(10)
print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x * 2 + 10, foo)
print reduce(lambda x, y: x + y, foo)

#if __name__ == "__main__":