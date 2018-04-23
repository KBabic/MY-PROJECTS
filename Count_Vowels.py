text = str(input("Enter a string: "))
print('\n')
vowels = ['a','e','i','o','u']

for vowel in vowels:
    print(f'Sum of vowel {vowel} found is: {text.count(vowel)}')