#!/usr/bin/python3
"""
Module contains find_peak()
"""


def recurse_peak(array, mid):
    """
    Recurses list to find peak
    """
    try:
        if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
            return array[mid]
        if array[mid + 1] > array[mid]:
            return recurse_peak(array, mid + 1)
        if array[mid - 1] > array[mid]:
            return recurse_peak(array, mid - 1)
    except Exception:
        pass


def find_peak(list_of_integers):
    """
     finds a peak in a list of unsorted integers
    """
    array = list_of_integers
    if not array:
        return None
    if len(array) == 1:
        return array[0]
    peak = None
    if array[0] >= array[1]:
        peak = array[0]
    if array[-1] >= array[-2]:
        peak = array[-1]

    new_peak = recurse_peak(array, (len(array) - 1) // 2)
    if new_peak:
        peak = new_peak

    return peak