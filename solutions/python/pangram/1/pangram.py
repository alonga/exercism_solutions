from string import ascii_lowercase

def is_pangram(s):
    return all(c in s.lower() for c in ascii_lowercase)