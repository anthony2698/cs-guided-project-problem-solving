"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Your code here
    # given a string a number find max and min number
    # we have functions max and min but only work on non negative numeric strings
    # it's feasible that we might get a string of all negative number
    # because of negative numbers, we can't get away with not turning the string into numbers
    # once we have a list a nums, we can use max and min to calculate max and min
    str_digits = input_str.split(" ")
    int_digits = [int(num) for num in str_digits]
    return f"{max(int_digits)} {min(int_digits)}"

print(max_and_min("1 2 3 4 5"))
print(max_and_min("1 2 -3 4 5"))
print(max_and_min("1 9 3 4 -5"))


