import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
i=0
url= input('Enter the url: ')
uh = urllib.request.urlopen(url, context=ctx)
data=uh.read()
tree = ET.fromstring(data)
comment=tree.findall('comments/comment')
for item in comment:
 count=(item.find('count').text)
 i+=1
 sum+=int(count)
print('count:',i)
print('sum:',sum)
