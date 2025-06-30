#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range (1):
            print("{:2d}{:2d}{:2d}".format(matrix[i][j],matrix[i][j+1],matrix[i][j+2]))
