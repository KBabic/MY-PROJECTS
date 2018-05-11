from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.nytimes.com/'
headers = {}
headers ['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
data = resp.read()
soup = BeautifulSoup(data)

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace('\n',' ').strip())
    else:
        print(story_heading.contents[0].strip())
