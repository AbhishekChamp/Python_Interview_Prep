# from typing import runtime_checkable


# Input Format:
#     Integer number
    
# Output Format:
#     Display nice number as per given rule
    
# Code Constraints:
#     1 <= Current Number <= 9999

# Rule:
#     Palindrome upto 9999 from the first number
    
# Input:
#     8758
    
# Output:
#     8778
#     8888
#     8998
#     9009
#     9119
#     9229
#     9339
#     9449
#     9559
#     9669
#     9779
#     9889
#     9999



def generatePalindrome(num):
    temp = int(num)
    while (temp <= 9999):
        num = str(temp)
        if(num[::1] == num[::-1]):
            print(num)
        temp += 1

number = input("Enter a number: ")

generatePalindrome(number)
