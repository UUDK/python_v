# Write a unittest file that tests the function in the script

import pytest

from count_vowels import count_vowels

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    ...

def test_count_vowels_all_vowels():
    ...

def test_count_vowels_mixed_case():
    ...

def test_count_vowels_mixed_characters():
    ...

def test_count_vowels_numbers_and_symbols():
    ...

def test_count_vowels_long_text():
    ...

@pytest.mark.skip(reason="This test is not implemented yet.")
def test_count_vowels_unicode():
    text = "Python jest językiem programowania"
    ...

# @pytest.mark.xfail(reason="This test is expected to fail.")
def test_count_vowels_fail():
    assert count_vowels("aeiouy") == 99
