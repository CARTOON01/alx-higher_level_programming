#!/usr/bin/python3
def best_score(a_dictionary):
    # Initialize variables to keep track of the best score and key
    best_key = None
    best_score = float('-inf')  # Start with negative infinity as the initial score

    # Iterate over each key-value pair in the dictionary
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            # If the current value is greater than the best score, update the best score and key
            if value > best_score:
                best_score = value
                best_key = key

    return best_key
