"""
Challenge #9:
​
Given a string, write a function that returns the "middle" character of the
word.
​
If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.
​
Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
​
​
# to find out if the string length is even we could decompose the logic in to it's own function
​
# we will need to find out the length of the string and set it to str_len
# to get the middle / mean index of the string length we can divide the str_len by 2 and set it to middle_index
# to make sure the number is usable as an index we want to floor it
# in python we have a floor divide //
​
# in the case of even length
    # return a slice of [middle_index - 1: middle_index + 1]
# in the case of odd Length
    # return a slice of [middle_index: middle_index + 1]
​
"""
def is_even(num):
    """
    takes in a number and checks if it is even
    then returns a boolean value of True if even and False if odd
    example: is_even(2) => True
    """
    return num % 2 == 0
​
def get_middle(input_str:str) -> str:
    # Your code here
    # we will need to find out the length of the string and set it to str_len
    str_len = len(input_str)
    # to get the middle / mean index of the string length we can divide the str_len by 2 and set it to middle_index
    # to make sure the number is usable as an index we want to floor it
    # in python we have a floor divide // in JS / TS `Math.floor` method to do a similar thing
    middle_index = str_len // 2
​
    # in the case of even length
    if is_even(str_len):
        # return a slice of [middle_index - 1: middle_index + 1]
        return input_str[middle_index - 1: middle_index + 1]
    # in the case of odd Length
    else:
        # return a slice of [middle_index: middle_index + 1]
        return input_str[middle_index: middle_index + 1]
​
​
​
print(get_middle("test")) # -> "es"
print(get_middle("testing")) # -> "t"
print(get_middle("middle")) # -> "dd"
print(get_middle("A"))  # -> "A"
​
​
"""
__something__ means private
​
​
"""