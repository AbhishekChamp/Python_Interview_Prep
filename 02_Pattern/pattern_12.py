# Input: 5

# Output:
#     * * * * * * * * *
#       * * * * * * *
#         * * * * *
#           * * *
#             *
            
# Inverted full pyramid

number = int(input("Enter the number: "))
size = 2 * number - 1
space = 0
for i in range(number):
    for j in range(space):
        print(end=" ")
    for j in range(size):
        print("*",end=" ")
    print()
    space += 2
    size -= 2        