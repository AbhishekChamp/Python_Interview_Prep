# Input: 4

# Output:
    
#     * * * * * * *
#     b * i i i * b
#     b b * i * b b
#     b b b * b b b
    
#     Hollow-pyramid inverted

number = int(input("Enter the number: "))

line_elements = 2*number-1

for i in range(number):
    for j in range(line_elements):
        
        right_index = line_elements-i-1         #Finding the position where the first * occus after i
        
        if (i == 0 or i == j or right_index == j):
            print("*", end=" ")
        
        elif (i < j and right_index > j):
            print("i",end=" ")
        
        else:
            print("b",end=" ")
    print()