# Input: 5

# Output: 
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#     * * *       * * *
#     * * *       * * *
#     * * *       * * *
#
#   Base 3 lines remains the same

number = int(input("Enter a number: "))

space = 2 * number - 2

for i in range(number+3):
    # Printing triangle
    if(number > i):
        for j in range(space):
            print(end=" ")
        for j in range(2*i+1):
            print("*", end=" ")
        space -= 2
    # Printing base
    else:
        for j in range(3):
            print("*",end=" ")
        for j in range(4*number-14):    # Number of spaces required in the base
            print(end=" ")
        for j in range(3):
            print("*", end=" ")
    print()
