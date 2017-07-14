from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
xml = urlopen(url, context=ctx).read()
#print (xml)

#xml.decode()
tree = ET.fromstring(xml)
#print (tree)

Comm = tree.findall('comments/comment')
#print (Comm)
print ('Comment Count: ',len(Comm))

lis = []
for element in Comm:
    Comm_Count = element.find('count').text
    #print (Comm_Count)
    str2int = int(Comm_Count)
    print (str2int)
    lis.append(str2int)
    #print(lis)
    Total = sum(lis)
    print (Total)
