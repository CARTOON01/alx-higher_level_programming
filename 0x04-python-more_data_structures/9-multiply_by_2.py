#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create an empty dictionary to store the multiplied values
    new_dict = {}

    # Iterate over each key-value pair in the input dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and store it in the new dictionary
        new_dict[key] = value * 2

    return new_dict
