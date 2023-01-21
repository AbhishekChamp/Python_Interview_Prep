# Input Format:
#     Number to be checked in the first line
#     Number of the digit in the second line

# Output Format:
#     Yes or No

# Rule:
#     Check the number of digits with the input of second line

# Input:
#     987654
#     6
# Output:
#     Yes

number_to_check = input("Enter the number: ")
number_of_digits = int(input("Enter the number of digits: "))

if(len(number_to_check) == number_of_digits):
    print("Yes")
else:
    print("No")