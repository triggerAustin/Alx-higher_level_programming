#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []*len(matrix)
    for i in matrix:
        squared.append(list(map(lambda x: x*x, i)))
    return squared
