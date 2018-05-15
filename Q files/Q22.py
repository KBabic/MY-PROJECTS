# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
sentence = input('Enter a sentence: ')
words = dict()
for item in sentence.split():
    words[item] = words.get(item,0) + 1
for x,y in sorted([(k,v) for k,v in words.items()]):
    print(x,':',y)
