import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth(n):
    return n**5

def test_square():
    assert square(2)==4, "Test failed, square 2 should be 4"
    assert square(3)==9, "Test failed, square 2 should be 9"

def test_cube():
    assert cube(2)==8, "Test failed, cube 2 should be 8"
    assert cube(3)==27, "Test failed, cube 2 should be 27"

def test_fifth():
    assert fifth(2)==32, "Test failed, fifth 2 should be 32"
    assert fifth(3)==243, "Test failed, fifth 2 should be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")

