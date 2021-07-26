# Input Format:
#     Number in the first line

# Output Format:
#     Display the given  number as a special number or not
    
# Rule:
#     1 + 7 + 2 + 9 = 19
#     19 * 91 = 1729

# Input:
#     1729

# Output:
#     1729 is a special number

number = int(input("Enter the number: "))

num = number
sum_number = 0

while(num != 0):
    temp = int(num % 10)
    sum_number = sum_number + temp
    num = int(num / 10)

# Convert the sum_number to string and reversed it and converted it to int

reverse = int(str(sum_number)[::-1])

if ((sum_number * reverse) == number):
    print(f"{number} is a special number")
else:
    print(f"{number} is not a special number")
