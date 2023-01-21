# Input: 5

# Output:
#     *               *
#     * *           * *
#     * * *       * * *
#     * * * *   * * * *
#     * * * * * * * * *
#     * * * * * * * * *
#     * * * *   * * * *
#     * * *       * * *
#     * *           * *
#     *               *

number = int(input("Enter the input: "))
space = 2 * number - 3

def print_star(val):
    for j in range(val):
        print("*",end=" ")

def print_space(val):
    for j in range(val):
        print(end="  ")

#Upper Part
for i in range(number):
    print_star(i+1)
    print_space(space)
    if (space != -1):
        print_star(i+1)
    else:
        print_star(i)
    space -= 2
    print()

space = -1
# Lower Part
for i in range(number, 0, -1):
    print_star(i)
    print_space(space)

    if (space != -1):
        print_star(i)
    else:
        print_star(i-1)

    space += 2
    print()