# Input: 5

# Output:
#     * * * * * * * * *
#     * * * *   * * * *
#     * * *       * * *
#     * *           * *
#     *               *
#     * *           * *
#     * * *       * * *
#     * * * *   * * * *
#     * * * * * * * * *

number = int(input("Enter a number: "))
size = 2 * number
star = number
space = 0

def print_star(val):
    for j in range(val):
        print("*",end=" ")

def print_space(val):
    for j in range(val):
        print(end="  ")

# Coding the upper part of pattern
for i in range(number):
    print_star(star)
    print_space(space)
    print_star(star)
    space+= 2
    star-= 1
    print()

star+= 2
space-= 4

# Coding the lower part of pattern
for i in range(1,number):
    print_star(star)
    print_space(space)
    print_star(star)
    space-=2
    star+=1
    print()