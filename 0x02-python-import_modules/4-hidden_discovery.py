#!/usr/bin/python3
import hidden_4 as hid

if __name__ == '__main__':
    names = filter(lambda n: not n.startswith('__'), dir(hid))
    for name in names:
        print(name)
