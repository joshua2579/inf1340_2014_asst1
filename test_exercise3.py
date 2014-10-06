#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that output the correct results
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    # other tests
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Scissors", "Paper") == 1

def test_input():
    """
    Inputs that are the correct value and type
    """
    with pytest.raises(ValueError):
        decide_rps("Rock","Sissors")
        decide_rps("Roc", "Scissors")
        decide_rps("something", "else")

    with pytest.raises(TypeError):
        decide_rps(2,"Scissors")
        decide_rps("Rock", 2.09)
        decide_rps(2.9876, 3.0987)

