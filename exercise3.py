#!/usr/bin/env python3


def decide_rps(player1, player2):
    """
    Returns the result of the game

    :params:
        player1 (string): Player 1's move
        player2 (string): Player 2's move

    :return:
        int: the result of the game

    :raises:
        ValueError if parameter is out of range
        ValueError if inputs are invalid
    """
    input_dictionary = {"Rock": 0, "Paper": 1, "Scissors": 2}
    # Check that the inputs are valid
    if player1 in input_dictionary and player2 in input_dictionary:
        player1_input = input_dictionary[player1]
        player2_input = input_dictionary[player2]

        result = player1_input - player2_input

        # The result is a tie.
        if result == 0:
            return 0
        # The result is that player 1 wins.
        elif result == 1 or result == -2:
            return 1
        # The result is that player 2 wins.
        elif result == -1 or result == 2:
            return 2
        # Some other result occurs.
        else:
            raise TypeError("Invalid result occurred")
    else:
        raise TypeError("Invalid inputs provided.")

