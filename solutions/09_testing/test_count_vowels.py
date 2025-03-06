# Write a unittest file that tests the function in the script

import pytest

from count_vowels import count_vowels

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_count_vowels_all_vowels():
    assert count_vowels("aeiouy") == 6

def test_count_vowels_mixed_case():
    assert count_vowels("AeIoUy") == 6

def test_count_vowels_mixed_characters():
    assert count_vowels("Hello, World!") == 3

def test_count_vowels_numbers_and_symbols():
    assert count_vowels("12345!@#$%") == 0

def test_count_vowels_long_text():
    text = "This is a longer piece of text with more vowels."
    assert count_vowels(text) == 15

@pytest.mark.skip(reason="This test is not implemented yet.")
def test_count_vowels_unicode():
    text = "Python jest językiem programowania"
    assert count_vowels(text) == 10

@pytest.mark.xfail(reason="This test is expected to fail.")
def test_count_vowels_fail():
    assert count_vowels("aeiouy") == 99
