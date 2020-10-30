"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :)
grin -> :D
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :)"
- emotify("Make me grin") ➞ "Make me :D"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.

- We might want to use a dictionary to store the key, value pairs
{
    'smile': ':)'
    'grin': ':D'
    'sad': ':('
    'mad': ':P'
}

- iterate over the hash table's items extrapolating the key and value of each item
- use a string '.replace' to replace the substring of the key with the value

"""


def emotify(txt):
    # store the key, value pair of the required data for swapping out the test to emoticons
    # we will store this data in a hash table (dictionary = Python | object = JS)
    data = {
        'smile': ':)',
        'grin': ':D',
        'sad': ':(',
        'mad': ':P',
    }
    # iterate over the hash table's items extracting the key and value
    for k, v in data.items():
        # set an updated string using the '.replace' method
        # return each txt with the old substring substituted for the old one
        txt = txt.replace(k, v)

    # return our new txt
    return txt



print(emotify("Make me smile")) # ➞ "Make me :)"
print(emotify("Make me grin")) # ➞ "Make me :D"
print(emotify("Make me sad")) # ➞ "Make me :("
print(emotify("Make me mad")) # ➞ "Make me :P"