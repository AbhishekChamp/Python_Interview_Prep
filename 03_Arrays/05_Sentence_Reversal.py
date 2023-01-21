# Problem Statment

# Given a string of words, reverse all the words.

# Input: "This is the best"
# Output: "best the is This"

# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as: '   space here' and 'space here    ' both become 'here space'

# Solution - 01
def rev_word(s):
    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))

# Solution - 02
def rev_word_2(s):
    return " ".join(reversed(s.split()))

# Solution - 03
def rev_word_3(s):
    return " ".join(s.split()[::-1])

# Testing solution
from nose.tools import assert_equal

class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol(' Hello John how are you  '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")

# Run and test
t = ReversalTest()
t.test(rev_word)