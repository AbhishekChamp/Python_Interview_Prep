# Input Format:
#     Input consists of 5 digit number
    
# Output Format:
#     Individual digits of the 5 digit number separated by 3 spaces each

# Input:
#     42139
    
# Output:
#     4   2   1   3   9


number = input("Enter the 5-digit number: ")
rev_num = int(number[::-1])

for i in range(5):
    print(rev_num % 10, end="   ")
    rev_num = rev_num // 10