# Input: 5

# Output:
#         *
#        * *
#       *   *
#      *     *
#     * * * * *
#
# Equilateral triangle

number = int(input("Enter the number: "))

for i in range(number):
    for j in range(2*number):
        if ((i+j == number-1) or (j-i == number-1)) and (i != number-1):
            print("*",end='')
        elif(i == number-1) and (j % 2 == 0):
            print("*", end='')
        else:
            print(end=" ")
    print()
