import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
for k,v in counts.items():
    if v == 1:
        print("The word '{}' appears {} time".format(k,v))
    else:
        print("The word '{}' appears {} times".format(k,v))
