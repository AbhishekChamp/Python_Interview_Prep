# Input: 5

# Output:
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *

number = int(input("Enter the number: "))

def print_star(val):
    for j in range(val):
        print("*",end=" ")
    print()
    
num = number
line_count = 2 * number
for i in range(1, line_count):
    if (i < number):
        print_star(i)
    else:
        print_star(num)
        num-= 1