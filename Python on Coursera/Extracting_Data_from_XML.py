import urllib.request
import xml.etree.ElementTree as ET
url = 'http://py4e-data.dr-chuck.net/comments_97961.xml'
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment/count')
count = len(lst)
count_sum = 0
for item in lst:
    num = int(item.text)
    count_sum += num
print('Retrieving ',url)
print('Retrieved', len(data), 'characters')
print('Count:', count)
print('Sum:', count_sum)
