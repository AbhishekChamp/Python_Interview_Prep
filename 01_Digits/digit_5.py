# from typing import ValuesView


# Input Format:
#     Integer number

# Output Number:
#     Binary, Octal and Hexadecimal Values
    
# Input:
#     23

# Output:
#     Binary Value : 10111
#     Octal Value : 27
#     Hexadecimal Value : 17

def convert(num, val,my_list):
    if num > val-1:
        convert(num//val, val,my_list)
    my_list.append(num % val)
    return my_list

def list_to_int(my_list):
    # Map with str function converts int list to string list
    # Join is used for converting string list to string
    # Int is used for converting string to int
    return int(''.join(map(str,my_list)))

number = int(input("Enter the number: "))

binary_val = convert(number, 2,[])
octal_val = convert(number,8,[])
hexadecimal_val = convert(number, 16, [])


print(f"Binary Value:{list_to_int(binary_val)}")
print(f"Octal Value:{list_to_int(octal_val)}")
print(f"Hexadecimal Value:{list_to_int(hexadecimal_val)}")
