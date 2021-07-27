# Input Format:
#     Input consists of binary number
    
# Output Format:
#     Output prints the corresponding decimal value
    
# Input:
#     111

# Output:
#     7

def convert_to_decimal(number):
    length = len(str(number))
    result = 0
    for i in range(length):
        result = result + (int(number % 10) * (2**i))
        number = number // 10
    return result

binary_num = int(input("Enter the binary number: "))

decimal_num = convert_to_decimal(binary_num)

print(decimal_num)