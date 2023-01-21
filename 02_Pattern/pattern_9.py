# Input: 4

# Output:
#     b b b * b b b
#     b b * i * b b
#     b * i i i * b
#     * * * * * * *
    
# Hollow Pyramid

number = int(input("Enter the number: "))

line_elements = 2 * number - 1
for i in range(number, 0, -1):
    right_index = line_elements-i
    for j in range(line_elements):
        if( (j == i-1) or (j == right_index) or (i==1)):
            print("*", end=" ")
        elif (i < j+1 and right_index > j):
            print("i", end=" ")
        else:
            print("b", end=" ")
    print()