# Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1, which is 10

def sum_func(n):
    if len(str(n)) == 1:
        return n
    else:
        # Strip another string
        return n%10 + sum_func(n//10)

# Testing Solution
result = sum_func(4321)
print(result)