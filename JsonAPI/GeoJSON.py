from urllib.request import urlopen
import urllib.parse
import json
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://xxxx'

while True:
    sensor = False
    address = input('Enter the address: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'sensor': sensor, 'address': address})
    print ('Retrieving:', url)

    mainurl = urlopen(url).read().decode()
    #print (mainurl)
    print ('List_length: ', len(mainurl))

    try:
        js = json.loads(mainurl)
        print (js)
    except:
        js = None

    '''if not js or 'status' not in js or js['status'] != 'OK':
        print ('============Failed to Retrieve============')
        print (mainurl)
        continue
        '''
        
    print(json.dumps(js, indent=3))
    place_id = js['results'][0]['place_id']
    print(place_id)
