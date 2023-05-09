#!/usr/bin/python3
def pow(a, b):
    # If b is 0, return 1
    if b == 0:
        return 1

    # If a is negative and b is even, return NaN
    if a < 0 and b % 2 == 0:
        return float('nan')

    # Compute the power using repeated multiplication
    result = 1
    abs_b = abs(b)
    for i in range(abs_b):
        result *= a

    # If b is negative, return 1/result
    if b < 0:
        return 1/result

    # Otherwise, return the result
    return result
