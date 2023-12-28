# From the list of numbers , find the maximum and minumum number
import random
def get_num_list():
    list = []
    for x in range(20):
        list.append(random.randint(3,9))
    return list

def getMin(list):
    min_num = list[0]
    for x in list:
        if(x < min_num):
            min_num = x
    return min_num

def getMax(list):
    max_num = list[0]
    for x in list:
        if (x > max_num):
            max_num = x
    return max_num


if __name__ == '__main__':
    num_list = get_num_list()
    print(num_list)
    print("The maximum number is the list is  - ",getMax(num_list))
    print("The Minimum number in the list is  - ",getMin(num_list))