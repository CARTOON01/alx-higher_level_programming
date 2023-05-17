#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()
    # Iterate over each element in the input list
    for item in my_list:
        # Add the element to the set (sets only store unique values)
        unique_set.add(item)
    # Compute the sum of all elements in the set
    result = sum(unique_set)
    return result
