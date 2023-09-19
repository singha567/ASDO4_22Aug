""" test cases for lab_untitest """

from appcode import lab_unittest

def test_count():
    assert lab_unittest.count((2,3,4,3),3) == 2
    assert lab_unittest.count(["a","bcd","a","ef"],"a") == 2
    assert lab_unittest.count((-2,-3,-4,-3),3) == 0

def test_count_zeros():
	assert lab_unittest.count([0,0,0],0)==3

def test_count_string():
	assert lab_unittest.count(["a","a","a"],"a")==3

def test_count_minus():
	assert lab_unittest.count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert lab_unittest.count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2

