import pandas as pd
import string
def test_cleaning():
    # Task A: Load data/messy strings.csv into df raw.
    df = pd.read_csv('/Users/anikakumar/BU RISE/Day 3/Lab/anika-kum-lab-3-data-parsing/data/messy_strings.csv')
    print(df)
    # Task C: Apply it: df[’clean’] = clean strings(df[’raw’])
    df['clean'] = clean_strings(df['raw'])
    #     Task D: Compute on df[’clean’]:
    # - Total rows
    # - Unique count
    # - Most common string (value counts())
    print(f"Total rows: {len(df['clean'])}")
    print(f"Unique count: {df['clean'].nunique()}")
    value_counts = df['clean'].value_counts(sort=True)
    print(f"In the data, the commonly occuring name was: {value_counts.index[0]}") #sorted earlier
    return df['clean'].to_csv(index=False)
#Task B: Write clean strings(strings) that:
    # - Strips spaces
    # - Lower-cases
    # - Removes punctuation (!?,.;:)
    # - Drops empty entries
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