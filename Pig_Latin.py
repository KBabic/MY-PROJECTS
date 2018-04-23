import string

word = str(input("Enter a word for Pig Latin transformation: "))
print('\n')

alphabet = set(string.ascii_lowercase)
vowels = set(['a','e','i','o','u'])
consonants = alphabet.difference(vowels)

if word[0] in consonants:
    if word[1] in consonants:
        word = word[2:] + word[0:2] + 'ay'
    if word[1] in vowels:
        word = word[1:] + word[0:1] + 'ay'
elif word[0] in vowels:
    word = word + 'way'

print('Transformed word is:',word)