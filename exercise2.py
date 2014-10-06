#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    if type(upc) != str:
        # raise TypeError if not string
        raise TypeError("Input must be a string")
    # check length of string
    elif len(upc) != 12:
        # raise ValueError if not 12
        raise ValueError("Invalid UPC length")
    # generate checksum using the first 11 digits provided
    else:
        # add the odd digits together
        odd_sum = sum([int(x) for x in upc[::2]])

        # add the even digits together (12th digit not included)
        even_sum = sum([int(x) for x in upc[1:-1:2]])

        # multiply the odd sum by 3, add that to the even sum and
        # find the modulo 10 of the result
        mod = ((odd_sum * 3) + even_sum) % 10

        # if the result is not 0, subtract the result from 10
        checksum_digit = 0
        if mod != 0:
            checksum_digit = 10 - mod

        # check against the the twelth digit
        # return True if they are equal, False otherwise
        if int(upc[11]) == checksum_digit:
            return True
        else:
            return False