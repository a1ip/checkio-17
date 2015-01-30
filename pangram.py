import re
import string

def check_pangram(text):
    text = set(filter(lambda x: x in string.ascii_lowercase, text.lower()))
    alphabet = set(string.ascii_lowercase)
    return True if not len(alphabet - text) else False  

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
