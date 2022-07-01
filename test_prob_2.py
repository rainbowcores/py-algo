import pytest
from prob_2 import unrepeated

def test_removes_duplicates_alphabet():
    assert unrepeated(["a", "b", "c", "a", "b", "d"]) == ["a", "b", "c", "d"]

def test_removes_duplicates_numerals():
    assert unrepeated([4, 4, 3, 2, 3, 1]) == [4, 3, 2, 1]

def test_empty_input():
    with pytest.raises(TypeError):
        unrepeated()

def test_chars():
    assert unrepeated(["!", "!", "#", "#"]) == ["!", "#"]