# Input: 4

# Output:
#           * * * *
#         * * * *
#       * * * *
#     * * * *

number = int(input("Enter the number: "))

space = number - 1

for i in range(number):
    for j in range(space):
        print(end=" ")
    for j in range(number):
        print("*", end=" ")
    space -= 1
    print()