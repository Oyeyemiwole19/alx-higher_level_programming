#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv
    args.pop(0)
    argc = len(args)
    len1 = "{:d} argument".format(argc)
    if argc == 0:
        len1 += "s."
    elif argc == 1:
        len1 += ":"
    else:
        len1 += "s:"
        print(len1)
        for i, arg in enumerate(args):
            print("{:d}: {:s}".format(i+1, arg))
