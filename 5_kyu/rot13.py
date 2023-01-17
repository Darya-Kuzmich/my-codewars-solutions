# DESCRIPTION:
# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
#
# I found this joke on USENET, but the punchline is scrambled.
# Maybe you can decipher it? According to Wikipedia, ROT13
# (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate
# jokes on USENET.
#
# Hint: For this task you're only supposed to substitue characters.
# Not spaces, punctuation, numbers etc.
#
# Test examples:
#
# "EBG13 rknzcyr." -->
# "ROT13 example."
#
# "This is my first ROT13 excercise!" -->
# "Guvf vf zl svefg EBG13 rkprepvfr!"

import string


class LettersRing:

    def __init__(self):
        self.data = string.ascii_lowercase
        self.size = len(self.data)

    def get_letter(self, idx: int) -> str:
        return self.data[idx % self.size]


def rot13(message: str) -> str:
    case = {
        'lower': lambda sym: sym.lower(),
        'upper': lambda sym: sym.upper(),
    }
    ring = LettersRing()
    res = ''
    for char in message:
        if char.lower() in ring.data:
            letter_case = 'lower' if char.islower() else 'upper'
            idx = ring.data.index(char.lower())
            char = ring.get_letter(idx + 13)
            char = case[letter_case](char)
        res += char
    return res
