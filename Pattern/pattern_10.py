# Input: 5

# Output:
#             *
#           * * *
#         * * * * * 
#       * * * * * * *
#     * * * * * * * * *
#     * * * * * * * * *
#       * * * * * * *
#         * * * * *
#           * * *
#             *
            
# Diamond

number = int(input("Enter the number: "))

space = 2 * number - 2

def print_star(val):
    for j in range(val):
        print("*",end=" ")

def print_space(val):
    for j in range(val):
        print(end=" ")

# Upper triangle
for i in range(number):
    print_space(space)
    print_star(2*i+1)
    space -= 2
    print()

space += 2

# Lower triangle
for i in range(number, 0, -1):
    print_space(space)
    print_star(2*i-1)
    space += 2
    print()