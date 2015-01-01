
"""Test count_evens module."""  

from count_evens import count_evens

def test_evens():
    x = [1, 2, 3, 4, 5, 7]
    assert count_evens(x) == 2
