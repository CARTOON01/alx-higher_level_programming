#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the value if the key already exists in the dictionary
    if key in a_dictionary:
        a_dictionary[key] = value
    # Add a new key/value pair if the key doesn't exist in the dictionary
    else:
        a_dictionary[key] = value

    return a_dictionary
