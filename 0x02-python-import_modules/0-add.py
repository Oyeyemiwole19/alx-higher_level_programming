#!/usr/bin/python3
if __name == "__main__":
    from add_0 import add
    def add(a, b):
        a = 1
        b = 1
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

