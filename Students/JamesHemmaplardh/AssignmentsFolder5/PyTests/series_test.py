
"""Test lucas, fibonacci, sum_series in series module."""  

import pytest
from series import lucas, fibonacci, sum_series

def test_lucas():
    x = 5
    assert lucas(x) == 11

def test_fibonacci():
	x = 7
	assert fibonacci(x) == 13

def test_sum_series():
	x = 3
	y = 4
	z = 3
	assert sum_series(x, y, x) == 10

