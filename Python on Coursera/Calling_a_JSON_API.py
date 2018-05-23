import json
import urllib.request, urllib.parse

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
    url = serviceurl + urllib.parse.urlencode({'address':address})
    data = urllib.request.urlopen(url).read().decode()
    char_count = 0
    for char in data:
        char_count += 1
    js = json.loads(data)
    place_id = js['results'][0]['place_id']
    print('Retrieving',url)
    print('Retrieved {} characters'.format(char_count))
    print('Place id: ',place_id)
