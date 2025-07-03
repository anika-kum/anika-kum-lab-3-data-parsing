import string
def clean_strings(strings):
    strings = strings.dropna() # remove missing/null value cells
    strings = strings.astype(str) # cast to string type
    strings = strings.str.strip() # clip leading and trailing whitespace
    strings = strings.str.lower() # convert everything to lowercase
    returnstring = []
    for s in strings:
        s = s.translate(str.maketrans("","",string.punctuation))
        returnstring.append(s)
    return returnstring
    
def test_special_chars():
    assert clean_strings(['anika!', 'kumar'], 0.0) == ['anika', 'kumar']

def test_casing():
    assert clean_strings(['AnIkA', 'kUmAr'], 0.0) == ['anika', 'kumar']

def test_whitespace():
    assert clean_strings([' anika', ' kumar'], 0.0) == ['anika', 'kumar']
    assert clean_strings([' ', ' '], 0.0) == ['', '']

def test_empty():
    assert clean_strings(['', ''], 0.0) == ['', '']


def test_numbers():
    assert clean_strings([1234, 1234], 0.0) == ['1234', '1234']