""" test cases for lab_untitest """

from appcode import lab_unittest

def test_count():
    assert lab_unittest.count((2,3,4,3),3) == 2
    assert lab_unittest.count(["a","bcd","a","ef"],"a") == 2
    assert lab_unittest.count((-2,-3,-4,-3),3) == 0