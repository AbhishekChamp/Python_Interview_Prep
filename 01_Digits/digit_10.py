# Input Format:
#     Input consists of single number
    
# Output Format:
#     Number is valid number or not
    
# Rule:
#     145 => 1! + 4! + 5! = 1 + 24 + 120 = 145
    
# Input:
#     145

# Output:
#     145 is a valid number

def fact(n):
    if(n > 1):
        return n* fact(n-1)
    return n

number = int(input("Enter the number: "))

num = number
fact_sum = 0

while (num != 0):
    fact_sum = fact_sum + fact(num % 10)
    num = num // 10

if number == fact_sum:
    print(f"{number} is a valid number.")
else:
    print(f"{number} is not a valid number")