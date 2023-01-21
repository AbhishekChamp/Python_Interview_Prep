# Input: 5

# Output:
#     *
#     * * *
#     * * * * *
#     * * * * * * *
#     * * * * * * * * *
    
number = int(input("Enter the number: "))

for i in range(number):
    for j in range(2*i + 1):
        print("*", end=" ")
    print()