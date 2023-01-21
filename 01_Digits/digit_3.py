# Input Format:
#     First line of the input consists of integer
    
# Output Format:
#     Sum of first and last digit and number of digits
    
# Input:
#     1221
    
# Output:
#     Sum of first and last digits : 2
#     Number of digits : 4

number = input("Enter the number: ")    #Input taken as string

number_of_digits = len(number)

first_digit = int(number[:1])
last_digit = int(number[number_of_digits-1:])

sum_of_first_last = first_digit + last_digit

print(f"Sum of first and last digits: {sum_of_first_last}")
print(f"Number of digits : {number_of_digits}")