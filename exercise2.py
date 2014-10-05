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
    if len(upc) != 12:
        # raise ValueError if not 12
        raise ValueError("Invalid UPC length")
    # generate checksum using the first 11 digits provided
    # add the odd digits together
    odd_digits = [upc[0], upc[2], upc[4], upc[6], upc[8], upc[10]]
    odd_sum = sum([int(x) for x in odd_digits])
    # add the even digits together (12th digit not included)
    even_digits = [upc[1], upc[3], upc[5], upc[7], upc[9]]
    even_sum = sum([int(x) for x in even_digits])
    # multiply the odd sum by 3 and add that to the even sum
    total_sum = (odd_sum * 3) + even_sum
    # find the total sum modulo 10
    mod = total_sum % 10
    # if the result is not 0, subtract the result from 10
    if mod != 0:
        checksum_digit = 10 - mod
    else:
        checksum_digit = 0
    # check against the the twelfth digit
    # return True if they are equal, False otherwise
    if int(upc[11]) == checksum_digit:
        return True
    else:
        return False