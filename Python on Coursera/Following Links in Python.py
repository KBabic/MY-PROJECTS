import urllib.request
from bs4 import BeautifulSoup
import re
base_url = 'http://py4e-data.dr-chuck.net/known_by_Teighan.html'
count = 7
position = 18

def retrieve(url):
    for i in range(1,count+1):
        print('Retrieving:', url)
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html)
        links = soup('a')
        link_position = 0
        for link in links:
            link_position += 1
            if link_position == position:
                url = link.get('href')
    print('The last name is:', re.findall('http://py4e-data.dr-chuck.net/known_by_(.*).html', url))

retrieve(base_url)   
