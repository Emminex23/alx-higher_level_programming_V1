#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list_sum = 0
    for i in set(my_list):
        new_list_sum += i
    return new_list_sum
