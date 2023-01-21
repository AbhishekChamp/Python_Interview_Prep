# Problem Statment

# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

# Input: finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
# Output: 5

# Solution - 01
def finder(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the array
    for num in arr1+arr2:
        result ^= num
    return result

# Solution - 02
import collections
def finder_2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1
    
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# Solution - 03
def finder_3(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 !=num2:
            return num1
    
    return arr1[-1]

# Testing Solution
from nose.tools import assert_equal

class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print("ALL TEST CASES PASSED")

# Run test
t = TestFinder()
t.test(finder)