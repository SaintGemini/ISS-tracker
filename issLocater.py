import json
import urllib.request
from threading import *
import time

astronauts = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(astronauts)
result = json.loads(response.read())
names = result['people']
print('People in Space', result['number'])
for p in names:
    print(p['name'])

def repeatISS():
    while(True):
        isslocation = 'http://api.open-notify.org/iss-now.json'
        response2 = urllib.request.urlopen(isslocation)
        endresult = json.loads(response2.read())
        location = endresult['iss_position']
        lat = location['latitude']
        lon = location['longitude']
        print('Latitude: ', lat)
        print('Longitude: ', lon)
        time.sleep(5)

t = Timer(5.0, repeatISS)
t.start()
