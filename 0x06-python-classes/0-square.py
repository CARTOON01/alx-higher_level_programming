#!/usr/bin/python3

"""This module defines a Square class"""

class Square:
    """This class represents a square"""

    def __init__(self, side_length):
        """Initialize the Square object with a given side length"""
        self.side_length = side_length

    def area(self):
        """Calculate and return the area of the square"""
        return self.side_length ** 2

    def perimeter(self):
        """Calculate and return the perimeter of the square"""
        return 4 * self.side_length
