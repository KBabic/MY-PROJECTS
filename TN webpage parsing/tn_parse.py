import urllib.request
import urllib.parse
import re
import string

# web page from which I want to extract only paragraphs out of html:
url = "http://tangonatural.com/en/10-reasons-to-dance-tango/"

# making sure I won't get an HTTP 403 Error
headers = {}
headers ['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
req = urllib.request.Request(url, headers = headers)

resp = urllib.request.urlopen(req)
respData = resp.read()

# extracting only normal text in paragraphs:
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

# saving extracted paragraphs into a new text file:
saveFile = open('tn_paragraphs.txt','w')
for eachParagraph in paragraphs:
	saveFile.write(str(eachParagraph))
saveFile.close()


