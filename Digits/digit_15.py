# Input Format:
#     Integer as a number
    
# Output Format:
#     Sum of digits till the sum is single digit
    
# Input:
#     5409

# Output:
#     9

def single_digit_sum(n):
    sum_val = 0
    while(n > 0):
        sum_val = sum_val + int(n % 10)
        n = n // 10
    return sum_val
    
    
number = int(input("Enter the number: "))

result = single_digit_sum(number)

while (result > 10):
    result = single_digit_sum(result)
    
print(result)
