
"""Test Ackermans module."""  

import pytest
from ack import ack

def test_ack():
    x = 3
    y = 5
    assert ack(x, y) == 6


# >>> ack.ack(3, 5)
# 6
# >>> ack.ack(5, 9)
# 10
# >>> 