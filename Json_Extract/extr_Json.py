import json
from urllib.request import urlopen
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
json_str = urlopen(url, context=ctx).read()
#print (json)
json_str.decode()

strcture = json.loads(json_str)
#print (strcture)
print ('List_length: ',len(strcture))
#print (strcture["note"])
#print (strcture["comments"])
lis = []

for item in strcture['comments']:
    comment_count = (item['count'])
    #print (comment_count)
    str2int = int(comment_count)
    lis.append(str2int)
    total = sum(lis)
    print (total)
