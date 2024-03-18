#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        a = [0]*len(my_list)
        for i in range(len(my_list)):
            value = False
            if (my_list[i] % 2) == 0:
                value = True
            a[i] = value
        return a
