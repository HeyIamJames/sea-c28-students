import pytest
from count_evens import count_evens

def test_count_evens():
    x = [1, 2, 3, 4, 5]
    assert count_evens(x) == 3
