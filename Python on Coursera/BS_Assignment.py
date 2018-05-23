from bs4 import BeautifulSoup
import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_97959.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
spans = soup('span')
spans_sum = 0
for tag in spans:
    x = int(tag.contents[0])
    spans_sum += x
print(spans_sum)
