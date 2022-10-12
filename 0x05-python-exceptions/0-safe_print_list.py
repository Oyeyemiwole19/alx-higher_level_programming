#!/usr/bin/python3
def safe_print_integer(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
        except indexError:
        break
        else:
        counter += 1

        print()
        return counter
