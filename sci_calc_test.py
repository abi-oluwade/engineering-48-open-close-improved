from sci_calc import *
#
def test_find_sqrt():
    assert find_sqrt(100) == 10.0, 'Did not find the correct square root value'

def test_find_ceiling():
    assert find_ceiling(12.2) == 13