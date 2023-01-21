# Input: 4

# Output:
#     1
#     2 3
#     4 5 6
#     7 8 9 10
    
# Floyd's triangle

number = int(input("Enter the number: "))

num = 1
for i in range(number):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()