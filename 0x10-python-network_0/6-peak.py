#!/usr/bin/python3
"""
    a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
        find the peal in an array using binary search
        time complexity O(log n)
        Args:
            list_pf_integers: array
    """
    size = len(list_of_integers)

    if !size:
        return None
    
    arr = list_of_integers
    mid_idx = size // 2

    while True:
        left = mid_idx - 1
        right = mid_idx + 1

        if (arr[mid_idx] > arr[left] and arr[mid_idx] > arr[right]
            or mid_idx == size - 1 or mid_idx == 0):
            return arr[mid_idx]
        if (arr[mid_idx] < arr[left]):
            mid_idx = left
        if (arr[mid_idx] < arr[right]):
            mid_idx = right
