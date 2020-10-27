"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    # count number of vowels
    # keep a counter to keep track of vowels
    # we need to inspect every char in string
    # keep a list or string of all the vowels we care about
    # iterate through the characters of our input string
        # as we iterate we can check if the current char is a part of the vowel string/list
        # if it is increment counter
    # return counter
    count = 0
    vowels = 'aeiou'
    for char in input_str:
        if char in vowels:
            count += 1
        
    return count

print(get_count("aeioufff"))
        
