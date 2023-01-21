# Problem Statment

# Given an array of integers (positive and negative) find the largest continuous sum

# Input: large_cont_sum([1, 2, -1, 3, 4, 10, 10, 10, -10, -1])
# Output: 29

# Solution
def large_cont_sum(arr):

    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

# Testing solution
from nose.tools import assert_equal

class LargeContTest(object):
    
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print("ALL TEST CASES PASSED")

# Run Test
t = LargeContTest()
t.test(large_cont_sum)