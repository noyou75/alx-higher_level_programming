#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = a[0]
    if len(my_list) == 0:
        return None
    for x in my_list[1:]:
        if x > largest:
            largest = x
    return largest