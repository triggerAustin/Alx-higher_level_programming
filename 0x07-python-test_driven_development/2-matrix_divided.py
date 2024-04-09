#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    matrix_divided: divides all elements of the matrix by div
    
    Args:
        @matrix: the list of elements
        @div: number to divide elements by

    Raises:
        TypeError: if Div is not integer, if matrix is not a list of integers
                    if row lengths is not equal
        ZeroDivisionError: if div is 0
    
    Return:
        matrix_2 of divided values
    """
    new_matrix = []
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) and \
            not any(map(lambda row: \
            any(not isinstance(x, (float, int)) for x in row), matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row=[]
        for element in row:
            new_row.append(element / div)
        new_matrix.append(new_row)

    return new_matrix
