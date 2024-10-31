# Note: all files to be run by pytest must start with test_*.py

import pytest
import sys

sys.path.append("../src")

from src.simpleutils import add_numbers

# ------------- Test cases for valid inputs -------------
# Test cases usually follow the structure of:
# 1. Define the expected result
# 2. Call the function with the input
# 3. Assert that the result is equal to the expected result
# The assert statement will raise an AssertionError if the result is not equal to the expected result
# The test will fail if an AssertionError is raised
# The test will pass if no AssertionError is raised
# Note: Functions must start with test_* to be recognized by pytest

def test_add_numbers_positive_numbers():
    expected = 3
    result = add_numbers(1, 2)
    assert result == expected

def test_add_numbers_negative_numbers():
    expected = -3
    result = add_numbers(-1, -2)
    assert result == expected

def test_add_numbers_mixed_numbers():
    expected = 0
    result = add_numbers(-1, 1)
    assert result == expected

def test_add_numbers_zero():
    expected = 0
    result = add_numbers(0, 0)
    assert result == expected

def test_add_numbers_large_numbers():
    expected = 3000000
    result = add_numbers(1000000, 2000000)
    assert result == expected

def test_add_numbers_float_numbers():
    expected = 3.5
    result = add_numbers(1.5, 2.0)
    assert result == expected

def test_add_numbers_large_negative_numbers():
    expected = -3000000
    result = add_numbers(-1000000, -2000000)
    assert result == expected

def test_add_numbers_large_mixed_numbers():
    expected = 0
    result = add_numbers(1000000, -1000000)
    assert result == expected

def test_add_numbers_small_numbers():
    expected = 0.0003
    result = add_numbers(0.0001, 0.0002)
    assert round(result, 4) == expected

def test_add_numbers_large_float_numbers():
    expected = 3000000.5
    result = add_numbers(1000000.25, 2000000.25)
    assert result == expected

# ------------- Test cases for invalid inputs -------------
def test_add_numbers_string_and_number():
    with pytest.raises(TypeError):
        add_numbers(1, "a")

def test_add_numbers_none_and_number():
    with pytest.raises(TypeError):
        add_numbers(None, 1)

def test_add_numbers_list_and_number():
    with pytest.raises(TypeError):
        add_numbers([1, 2], 3)

def test_add_numbers_dict_and_number():
    with pytest.raises(TypeError):
        add_numbers({"key": "value"}, 1)

def test_add_numbers_tuple_and_number():
    with pytest.raises(TypeError):
        add_numbers((1, 2), 3)

# ------------- Additional test cases for edge cases -------------

def test_add_numbers_max_integer():
    expected = sys.maxsize + 1
    result = add_numbers(sys.maxsize, 1)
    assert result == expected

def test_add_numbers_min_integer():
    expected = -sys.maxsize - 2
    result = add_numbers(-sys.maxsize - 1, -1)
    assert result == expected

def test_add_numbers_infinity():
    expected = float('inf')
    result = add_numbers(float('inf'), 1)
    assert result == expected

def test_add_numbers_negative_infinity():
    expected = float('-inf')
    result = add_numbers(float('-inf'), -1)
    assert result == expected

def test_add_numbers_nan():
    result = add_numbers(float('nan'), 1)
    assert result != result  # NaN is not equal to itself

def test_add_numbers_large_exponent():
    expected = 1e308 + 1e308
    result = add_numbers(1e308, 1e308)
    assert result == expected

def test_add_numbers_small_exponent():
    expected = 1e-308 + 1e-308
    result = add_numbers(1e-308, 1e-308)
    assert result == expected