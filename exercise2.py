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


def checksum (upc):
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
    upc = str(upc)
    if upc != str(upc):
        # raise TypeError if not string
        raise TypeError ("Input must be a string")
    # check length of string
    if len(upc) !=12:
        # raise ValueError if not 12
        raise ValueError ("Invalid UPC length")

    # convert string to array
    # hint: use the list function

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit

    # return True if they are equal, False otherwise

    return False

