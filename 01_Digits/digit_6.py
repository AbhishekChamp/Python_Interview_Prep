# Input Format:
#     Number in first line
#     Task Code in the second line
    
# Output Format:
#     Display the result as per task code
    
# Code Constraints:
#     Choice code is A/B/C/D
    
# Rule:
#     A - To calculate the sum of first and last digits of the given number
#     B - To check number is palindrome or not
#     C - To count the number of digits in the given number
#     D - To print it into words
    
# Input:
#     5232
#     A
    
# Output:
#     Sum of first and last digit: 7
    
def choice_A(num):
    first = int(num[:1])
    last = int(num[len(num)-1: :1])
    print(f"Sum of first and last digit : {first+last}")


def choice_B(num):
    if(num == num[::-1]):
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not a palindrome")

def choice_C(num):
    print(f"Total number of digits : {len(num)}")
    

def choice_D(num):
    val = int(num[::-1])
    word = ['Zero','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    while(val!=0):
        choice = val % 10
        print(word[choice],end= " ")
        val = val // 10

number = input("Enter the number: ")
choice = input("Enter your choice: ")

if choice == 'A':
    choice_A(number)
elif choice == 'B':
    choice_B(number)
elif choice == 'C':
    choice_C(number)
elif choice == 'D':
    choice_D(number)
else:
    print("Invalid choice")
