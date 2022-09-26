#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        format_i = " ".join(["{:d}" for x in i])
        print(format_i.format(*i))



if __name__ == '__main__':
    mat = [[a, a+1, a+2] for a in range(1, 16, 3)]
    print_matrix_integer(mat)
