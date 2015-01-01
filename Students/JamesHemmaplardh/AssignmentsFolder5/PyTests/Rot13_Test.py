
"""Test Rot13 module."""  

import pytest
from Rot13 import rot13

def test_rot13():
    assert rot13("I am, BaTman   ") == "V nz, OnGzna   "


# def test_rot13():
#     assert rot13("I am, BaTman   ") == V nz, OnGzna   "
# Enter Code:I am, BaTman   
# Out[12]: 'V nz, OnGzna   '