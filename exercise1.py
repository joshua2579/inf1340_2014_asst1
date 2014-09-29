#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def letter_to_gpa(letter_grade):
    """
    Returns the gpa for a given letter grade.

    :params:
        grade (integer): grade to be converted

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        ValueError if parameter is out of range
    """
    letter_grade_dictionary = {"A+": 4.0, 'A': 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "FZ": 0.0}
    gpa = 0.0
    # check that the grade is one of the accepted values
    if letter_grade in letter_grade_dictionary:
        # assign grade to letter_grade
        gpa = letter_grade_dictionary[letter_grade]
    else:
        # raise a ValueError exception
        raise ValueError("Invalid letter grade has been entered")
    return gpa


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0
    numeric_grade_list = [90, 85, 80, 77, 73, 70]
    letter_grade_list = ["A+", "A", "A-", "B+", "B", "B-"]

    if type(grade) is str:
        gpa = letter_to_gpa(grade)
    elif type(grade) is int:
        # check that grade is in the accepted range
        if grade in range(0,101):
            loop_iterator = 0
            letter_grade = "FZ"
            for number in numeric_grade_list:
                if (grade >= number):
                    # convert the numeric grade to a letter grade
                    letter_grade = letter_grade_list[loop_iterator]
                    break
                else:
                    loop_iterator += 1
            # assign value to GPA
            gpa = letter_to_gpa(letter_grade)
        else:
            # raise a ValueError exception
            raise ValueError("Invalid numerical grade has been entered")
    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")
    return gpa

