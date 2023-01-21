# Input: 5

# Output:
#             *
#             *
#             *
#             *
#     * * * * * * * * *
#             *
#             *
#             *
#             *

# number = int(input("Enter the number: "))

number = 5

for i in range(2*number-1):
    for j in range(2*number-1):
        if(j == number-1 or i == number-1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()