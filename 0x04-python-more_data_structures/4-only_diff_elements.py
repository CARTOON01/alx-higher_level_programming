#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    diff_set = set()

    # Iterate over each element in set_1
    for item in set_1:
        # If the element is not present in set_2, add it to the diff_set
        if item not in set_2:
            diff_set.add(item)

    # Iterate over each element in set_2
    for item in set_2:
        # If the element is not present in set_1, add it to the diff_set
        if item not in set_1:
            diff_set.add(item)

    return diff_set
