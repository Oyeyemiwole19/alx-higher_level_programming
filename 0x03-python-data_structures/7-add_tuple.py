#!/usr/bin/python3
def add_tuple(a=(), b=()):
    while len(a) < 2:
        a = (*a, 0)
        while len(b) < 2:
            b = (*b, 0)
            return a[0] + b[0], a[1] + b[1]
