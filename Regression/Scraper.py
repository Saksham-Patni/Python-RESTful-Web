from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#list1= list()
url = input ('enter the url: ')
print (url)

'''def loop():

    for element in tags:
        if (element == tags[2]):
            #print (element)
            global link
            link = element.get('href')
            #print(link)
            ls.append(link)

loop()

for ln in ls:
    while len(ls) < 5:
        html2 = urlopen(ln, context=ctx).read()
        #print (opn)
        soup = BeautifulSoup(html2, "html.parser")
        tags = soup('a')
        loop()

html3 = urlopen(ls[2], context=ctx).read()
        #print (opn)
soup = BeautifulSoup(html3, "html.parser")
tags = soup('a')
loop()

html4 = urlopen(ls[3], context=ctx).read()
        #print (opn)
soup = BeautifulSoup(html4, "html.parser")
tags = soup')
loop

print(ls) '''

for i in range (7):  # repeat 4 times
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    element = tags[17].get('href', None)
    url = element
    print (url)
