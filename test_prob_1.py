import pytest
from prob_1 import numeric

def test_removes_non_numeric():
    assert numeric("..2965a") == "2965"

def test_string_with_spaces():
    assert numeric("hello 12 hi 89")=="1289"

def test_string_with_no_numerals(): #should return empty string
    assert numeric("!!gbkejdk")==''
 
def test_int_input():
    assert numeric(2222)=="2222"

def test_empty_input():
    with pytest.raises(TypeError):
        numeric()