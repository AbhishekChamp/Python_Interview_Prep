# Input: 5

# Output:
#             1
#           2 3 2
#         3 4 5 4 3
#       4 5 6 7 6 5 4
#     5 6 7 8 9 8 7 6 5

number = int(input("Enter a number: "))

space = (2 * number) - 2        # Number of spaces

print(end=" ")                  # For aligning first line
for i in range(number):
    line_num = i                       # Copying the line number
    for j in range(space):
        print(end=" ")
    space-= 1                    # Reducing the space for next iteration
    for j in range(0, 2*i+1):
        if (i == j):
            print(2*i+1, end=" ")   # If equal 2*row number - 1 is printed
        elif( i > j):
            print(line_num+1, end=' ')     
            line_num+= 1                    # Increasing number by 1
        else:
            print(line_num, end=" ")
            line_num-= 1                    # Decreasing number by 1
    print()
