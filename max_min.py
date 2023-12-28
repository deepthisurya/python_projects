# From the list of numbers , find the maximum and minumum number
import random

#Generate a random number list
def get_num_list():
    list = []
    for x in range(20):
        list.append(random.randint(3,9))
    return list

#Function to get Minimum number in the list
def getMin(list):
    min_num = list[0]
    for x in list:
        if(x < min_num):
            min_num = x
    return min_num
#Function to get the Maximum number in the given list
def getMax(list):
    max_num = list[0]
    for x in list:
        if (x > max_num):
            max_num = x
    return max_num

#Main Function
if __name__ == '__main__':
    num_list = get_num_list()
    print(num_list)
    print("The maximum number is the list is  - ",getMax(num_list))
    print("The Minimum number in the list is  - ",getMin(num_list))