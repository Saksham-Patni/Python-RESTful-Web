import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Ignore SSL Certificate errors
contxt = ssl.create_default_context()
contxt.check_hostname = False
contxt.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
html = urlopen(url, context=contxt).read()
#print (html)

#http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")
#print (soup)

#Retrieve all the required tags
tags = soup('span')
#print (tags)
list_integers = list()

#Iterate over the integer list and calculate the sum
for tag in tags:
    i = tag.contents[0]
    integer= int(i)
    list_integers.append(integer)
    total = sum(list_integers)
    print (len(list_integers))
    print (total)


    '''def StrToInt_SumOfList():

        str_to_int = [int(i) for i in tag]
#        print(tags.count(i))

        list_integers.append(sum(str_to_int))
    #print (list_integers)

        total = sum(list_integers)
        print (total)

    StrToInt_SumOfList()
'''
