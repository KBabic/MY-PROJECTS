import sqlite3
import urllib.request
import re

url = 'https://www.py4e.com/code3/mbox.txt'
headers = dict()
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
req = urllib.request.Request(url, headers = headers)
file = urllib.request.urlopen(req).read().decode()

# establish connection to the DB and create a table:
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# get the list of e-mail domains (organizations) from the file (which is a string)
# --> where ever you find 'From:', extract all alphanumeric and non whitespace characters that come after '@':
domains = re.findall('From:.+@(\w+\S+)',file)
for org in domains:
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    # if there are no values in the table, insert them
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    # if there are values in the table, update them:
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?', (org,))
conn.commit()

for row in cur.execute('SELECT org, count FROM Counts ORDER BY count DESC'):
    print(row[0], str(row[1]))

cur.close()
