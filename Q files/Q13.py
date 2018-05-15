# Write a program that accepts a sentence and calculate the number of letters and digits.
import re
import string
alphabet = string.ascii_lowercase
ALPHABET = string.ascii_uppercase
sentence = input('Enter your sentence: ')
digits = re.findall('\d',sentence)
letters = list()
for char in sentence:
    if char in alphabet or char in ALPHABET:
        letters.append(char)
print('Digits:',len(digits))
print('Letters:',len(letters))


# another way:
# sentence = input('Enter your sentence')
# d = dict()
# for char in sentence:
    # if char.isdigit():
        # d['Digits'] = d.get('Digits',0) + 1
    # elif c.isalpha():
        # d['Letters'] = d.get('Letters',0) + 1
    # else:
        # pass
# print('Digits:',d['Digits'])
# print('Letters:',d['Letters'])
