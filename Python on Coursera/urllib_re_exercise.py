import urllib.request
import re
url = "http://www.py4e.com/book.htm"
headers = dict()
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
req = urllib.request.Request(url, headers = headers)
html = urllib.request.urlopen(req).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())
