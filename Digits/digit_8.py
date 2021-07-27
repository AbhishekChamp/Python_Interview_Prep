# Input Format:
#     Input consists of three integers
#     First input consists of 'k' digits to be printed
#     Second input consists of the number to be powered
#     Third value consists of the power value
    
# Output Format:
#     Prnt the last k digits of a^b

# Input:
#     2
#     11
#     3
    
# Output:
#     Last two digit(s) are 31

def find_word(val):
    my_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return my_list[val]

print("Enter the three integers: ")
k = int(input())
a = input()
b = input()


num = str(int(a) ** int(b))
print(num)

expected_result = num[k:]

word = find_word(k)

print(f"Last {word} digit(s) are {expected_result}")