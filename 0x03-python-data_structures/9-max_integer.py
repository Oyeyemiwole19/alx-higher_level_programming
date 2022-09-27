#!/usr/bin/python3
def max_integer(my_list=[]):
    L = len(my_list)
    if L == 0:
        return None
    Max = my_list[0]
    for item in my_list:
        if item > Max:
            Max = item
        return Max
