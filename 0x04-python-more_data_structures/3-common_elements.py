#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common_set = set()
    # Iterate over each element in set_1
    for item in set_1:
        # If the element is present in set_2, add it to the common set
        if item in set_2:
            common_set.add(item)
    return common_set
