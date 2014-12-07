

'''

The raw_input() function can generate two exceptions:
EOFError or KeyboardInterrupt on end-of-file (EOF) or canceled input.

Create a wrapper function, perhaps safe_input() that returns
None rather rather than raising these exceptions, when the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.
'''