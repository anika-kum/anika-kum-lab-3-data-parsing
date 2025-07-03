from string_utils import clean_strings
import pandas as pd

def test_special_chars():
    assert pd.Series(clean_strings(pd.Series(['anika!', 'kumar']))).equals(pd.Series(['anika', 'kumar']))

def test_casing():
    assert pd.Series(clean_strings(pd.Series(['AnIkA', 'kUmAr']))).equals(pd.Series(['anika', 'kumar']))

def test_whitespace():
    assert pd.Series(clean_strings(pd.Series([' anika', ' kumar']))).equals(pd.Series(['anika', 'kumar']))
    assert pd.Series(clean_strings(pd.Series([' ', ' ']))).equals(pd.Series(['', '']))

def test_empty():
    assert pd.Series(clean_strings(pd.Series(['', '']))).equals(pd.Series(['', '']))

def test_numbers():
    assert pd.Series(clean_strings(pd.Series([1234, 1234]))).equals(pd.Series(['1234', '1234']))