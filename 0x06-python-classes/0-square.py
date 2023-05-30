#!/usr/bin/python3
class Square:
    """This class represents a square"""

    def __init__(self, side_length):
        """Initialize the Square object with a given side length"""
        self.side_length = side_length

    def get_area(self):
        """Calculate and return the area of the square"""
        return self.side_length ** 2