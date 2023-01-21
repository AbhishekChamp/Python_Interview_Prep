# Problem Statment

# Given a string of opening and closing parentheses, check whether it's balaned. We have three types of parentheses: round brackets: (), square brackets: [], curly brackets: {}. Assume that the string doesn't contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example '([])' is balanced but '([(]' is not.

# Solution
def balance_check(s):
    
    if len(s)%2 != 0:
        return False
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0

# Testing solution
from nose.tools import assert_equal

class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print("ALL TEST CASES PASSED")

# Run Tests

t = TestBalanceCheck()
t.test(balance_check)