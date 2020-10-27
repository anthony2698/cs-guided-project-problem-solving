"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    # Your code here
    # if string is even, return middle 2 chars
    # elif string is odd, return middle char
    if len(input_str) % 2 == 0:
        return(input_str[(len(input_str) // 2) - 1 : 1 + (len(input_str) // 2)])
    else:
        return(input_str[len(input_str) // 2])

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))


