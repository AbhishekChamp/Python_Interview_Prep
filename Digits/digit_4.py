# Input Format:
#     Input consists of a number
    
# Output Format:
#     Output prints that the particular number is a palindrome or not
    
# Input:
#     2112
    
# Output:
#     2112 is a palindrome

number = input("Enter the number: ")

if(number[:] == number[::-1]):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")