# Input: 6

# Output:
#     0
#     0 1
#     0 2 4
#     0 3 6 9
#     0 4 6 12 16
#     0 5 10 15 20 25
#     0 6 12 18 24 30 36

# 0 to N multiplication

number = int(input("Enter the number: "))

for i in range(number+1):
    for j in range(i+1):
        print(i*j,end=" ")
    print()