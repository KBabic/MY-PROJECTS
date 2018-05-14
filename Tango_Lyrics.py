import urllib.request
from bs4 import BeautifulSoup
import string

alphabet = string.ascii_lowercase
# base url:
url = 'http://www.todotango.com/english/music/songs/lyrics/'

# list of all links to songs lyrics in alphabetic order:
urls = list()
for char in alphabet:
    link = url + char + '/0/todos/'
    urls.append(link)

# for link in urls: print(link)

headers = dict()
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

# list of words that should not be displayed:
skip_words = ['Log in','Register','Español', 'Deutsch','Português','The Music','The Artists','Carlos Gardel','The Dance','The Chronicles','The Community',
'Film Library', 'Music','Lyrics','Scores','Videos','Discographies','All','Tango','Milonga','Poem','Folklore','Waltz','Song','Other','Foxtrot','Tango music',
'Tango lyrics','Tango songs','Tango scores','Tango Artists','Tango Musicians','Tango Poets','Tango Singers','Tango Female singers','Tango Composers', 'About us',
'Contributors','Contact us','The Selection (Dec 2016)','The Selection (May-16)','The Selection (Nov-15)','The Selection (Jun 2015)','The Selection','Today´s music selection']
# there must be other way to exclude these words from the output!

tango_lyrics = open('C:\\Users\\Kaja\\Desktop\\PYTHON COURSERA\\tango_lyrics.txt','w+')
for link in urls:
    letter = alphabet[urls.index(link)].upper()
    req = urllib.request.Request(link, headers = headers)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html)
    tango_lyrics.write('\nSongs that start with {}:\n'.format(letter))
    for item in soup.find_all('a'):
        if len(item.text) > 1 and item.text.startswith(letter) and (not item.text in skip_words):
            tango_lyrics.write(item.text.strip()+'\n')

tango_lyrics.close()
