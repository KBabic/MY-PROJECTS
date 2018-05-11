import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
data = resp.read()
soup = BeautifulSoup(data)
web_page_text = open('C:\\Users\\Kaja\\Desktop\\MY-PROJECTS\\web_page_text.txt','w+')
for item in soup.find_all('p'):
    web_page_text.write(item.text + '\n')
web_page_text.close()
