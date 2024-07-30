#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """

    size = len(list_of_integers)

    if size == 0:
        return None
 
    arr = list_of_integers
    mid_idx = size // 2

    while True:
        left = mid_idx - 1 if mid_idx > 0 else 0
        right = mid_idx + 1 if mid_idx < size - 1 else size - 1

        if (arr[mid_idx] > arr[left] and arr[mid_idx] > arr[right]
                or mid_idx == size - 1 or mid_idx == 0):
            return arr[mid_idx]
        if (arr[mid_idx] < arr[left]):
            mid_idx = left
        if (arr[mid_idx] < arr[right]):
            mid_idx = right
