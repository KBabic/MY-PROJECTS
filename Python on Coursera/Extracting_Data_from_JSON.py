import urllib.request
import json

while True:
    url = input('Enter URL: ')
    if len(url) < 1:
        break
    req = urllib.request.urlopen(url).read()
    char_count = 0
    for char in req:
        char_count += 1

    data = json.loads(req)
    comment_counts = list()
    for item in data['comments']:
        comment_counts.append(int(item['count']))
    print('Retrieving', url)
    print('Retrieved {} characters'.format(char_count))
    print('Count:',len(comment_counts))
    print('Sum:', sum(comment_counts))
