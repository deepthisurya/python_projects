# This program tells us , the number user gives is even or odd

def isEven(num):
    if num%2 == 0:
        return "Number is even"
    else:
        return "Number is odd"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = isEven(int(input("Enter the number ! ")))
    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
