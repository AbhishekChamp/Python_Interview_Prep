# Input Format:
#     Integer Number
    
# Output Format:
#     Logged In or Incorrect Code
    
# Code Constrains:
#     No.of digits <= 3
    
# Rule:
#     Last 3 digit should be divisible by the first digit of the number

# Input:
#     2345

# Output:
#     Incorrect code
 
number = input("Enter the number: ")

first_digit = int(number[0])
last_three_digit = int(number[len(number)-3:])

if((last_three_digit % first_digit) == 0):
    print("Logged In")
else:
    print("Incorrect Code")