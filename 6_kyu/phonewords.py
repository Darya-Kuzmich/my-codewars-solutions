# DESCRIPTION:
# Given a string of numbers, you must perform a method in which you will
# translate this string into text, based on the phone keypad.
#
# For example if you get "22" return "b", if you get "222" you will return "c".
# If you get "2222" return "ca".
#
# Further details:
#
# 0 is a space in the string.
# 1 is used to separate letters with the same number.
# always transform the number to the letter with the maximum value, as long as
# it does not have a 1 in the middle. So, "777777" -->  "sq"
# and "7717777" --> "qs".
# you cannot return digits.
# Given a empty string, return empty string.
# Return a lowercase string.

# Examples:
# "443355555566604466690277733099966688"  -->  "hello how are you"
# "55282"                 -->  "kata"
# "22266631339277717777"  -->  "codewars"
# "66885551555"           -->  "null"
# "833998"                -->  "text"
# "000"                   -->  "   "

KEYPAD = {
    '0': [' '],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


def phone_words(strng: str) -> str:
    cnt = 0
    current = ''
    syms = []
    for sym in strng:
        if sym == current:
            cnt += 1
        elif sym == '1':
            cnt = 0
            continue
        else:
            current = sym
            cnt = 1
        syms.append((sym, cnt))

    for idx in range(1, len(syms)):
        if syms[idx][0] == syms[idx-1][0] and syms[idx][1] > syms[idx-1][1]:
            syms[idx-1] = None

    syms = [el for el in syms if el]

    letters = []

    for sym, cnt in syms:
        if sym == '0':
            letters.append(cnt * KEYPAD[sym][0])
        else:
            try:
                letters.append(KEYPAD[sym][cnt-1])
            except IndexError:
                whole_parts = cnt // len(KEYPAD[sym])
                remainder = cnt % len(KEYPAD[sym])
                for _ in range(whole_parts):
                    letters.append(KEYPAD[sym][-1])
                if remainder:
                    letters.append(KEYPAD[sym][remainder-1])
    return ''.join(letters)
