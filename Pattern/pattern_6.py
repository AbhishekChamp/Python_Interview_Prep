# Input: 5

# Output:
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
    
# Half-pyramid

number = int(input("Enter the number: "))

for i in range(number):
    for j in range(number):
        if (i >= j):
            print(j+1, end=" ")
    print()