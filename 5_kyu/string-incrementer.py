# DESCRIPTION:
# Your job is to write a function which increments a string, to create
# a new string.
#
# If the string already ends with a number, the number should be
# incremented by 1.
# If the string does not end with a number. the number 1 should be appended
# to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should
# be considered.

def increment_string(strng: str) -> str:
    if strng == '' or not strng[-1].isdigit():
        return f'{strng}1'

    digits = []
    for sym in strng[::-1]:
        if sym.isdigit():
            digits.append(sym)
        else:
            break

    digits.reverse()
    additional = str(int(''.join(digits)) + 1)
    if len(digits) > len(additional):
        return f'{strng[:-len(digits)]}{(len(digits) - len(additional)) * "0"}{additional}'  # noqa
    return f'{strng[:-len(digits)]}{additional}'
