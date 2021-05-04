import pytest
import test_me

def test_factorial():
    assert test_me.fact(0) == 6


def test_list_of_squares():
    assert test_me.list_of_squares(6) == 1
    assert test_me.list_of_squares(4) == 0