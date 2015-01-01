
"""Test Ackermans module."""  

from ack import ack

def test_ack():
    assert ack(3, 5) == 6
    assert ack(5, 9) == 10
    assert ack(-2, -3) == None 

# >>> ack.ack(3, 5)
# 6
# >>> ack.ack(5, 9)
# 10
# >>> 