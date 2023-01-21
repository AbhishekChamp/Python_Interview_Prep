# Input: 5

# Output:
#     1
#     0 1
#     1 0 1
#     0 1 0 1
#     1 0 1 0 1

number = int(input("Enter the number: "))
temp = 1

for i in range(number):
    for j in range(i+1):
        print(temp, end=" ")
        temp = 0 if temp == 1 else 1
    print()