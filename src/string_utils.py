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