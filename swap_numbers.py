#This program swaps the two numbers given by the users


# This function swaps the numbers received from the user
def swap_numbers(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    print("After swapping num1 - ", num1, " num2 -", num2)

#This function takes input of two numbers
def get_numbers_user():
    num1 = int(input("Enter Number 1 - "))
    num2 = int(input("Enter number 2 - "))
    print("Before swapping num1 - ", num1, " num2 -", num2)
    return num1,num2

#This is main function calling the swap function
if __name__ == '__main__':
    num1,num2 = get_numbers_user()
    swap_numbers(num1,num2)

