# DESCRIPTION:
# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text: str) -> str:
    words = text.split(' ')

    res = []
    for word in words:
        if word.isalpha():
            word = word[1:] + word[0] + 'ay'
        res.append(word)

    return ' '.join(res)
