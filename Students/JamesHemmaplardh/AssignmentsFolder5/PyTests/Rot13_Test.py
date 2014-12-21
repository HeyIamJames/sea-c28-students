
"""Test Rot13 module."""  

import pytest
from Rot13 import rot13

def test_rot13():
    assert rot13("i am batman") == "v nz ongzna"
