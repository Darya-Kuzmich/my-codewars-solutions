# DESCRIPTION:
# Complete the method/function so that it converts dash/underscore delimited
# words into camel casing. The first word within the output should be
# capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
# The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re


def to_camel_case(text: str) -> str:
    text = re.split('-|_', text)

    res = []

    for idx in range(len(text)):
        if idx > 0:
            res.append(text[idx].title())
        else:
            res.append(text[idx])

    return ''.join(res)
