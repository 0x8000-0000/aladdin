#!/usr/bin/env python3

# example: ./find_closest_sunrail_station.py 28.600574 -81.197851

import sys
import json
import urllib.request

class Station(object):

   def __init__(self, name, latitude, longitude):
      self.name = name
      self.latitude = latitude
      self.longitude = longitude

   def getMapzen(self):
      return { "lat": self.latitude, "lon": self.longitude }

sunrailLocations = [
    Station("Dummy", 0, 0),
    Station("Sanford", 28.8134755007, -81.2981154789),
    Station("Lake Mary", 28.7586649414, -81.3183007827),
    Station("Altamonte Springs", 28.6638272231, -81.3566132605),
    Station("Winter Park", 28.5974557336, -81.3516669263),
    Station("Florida Hospital Health Village", 28.5732723849, -81.3713926585),
    Station("LYNX Central", 28.548550531, -81.3808650474),
    Station("Orlando Health/Amtrak", 28.526087319, -81.3819822268),
    Station("Sand Lake Road", 28.4531540986, -81.3669846899),
    Station("Church Street", 28.5389007413, -81.3807703597),
    Station("Longwood", 28.7012989343, -81.3453776838),
    Station("Maitland", 28.6349429309, -81.3621632499),
    Station("DeBary", 28.8556935029, -81.3234127708),
]

request = {
    "costing": "pedestrian"
      }


startingPoint = [ { "lat": sys.argv[1], "lon": sys.argv[2] } ]

request["locations"] = startingPoint + list(map(lambda x: x.getMapzen(), sunrailLocations[1:]))
requestString = json.dumps(request, separators=(',',':'))

apiKey = 'mapzen-eDR41VF'

url = "https://matrix.mapzen.com/one_to_many?json=%s&id=sunrail_distance&api_key=%s" % (requestString, apiKey)

req = urllib.request.Request(url)
r = urllib.request.urlopen(req)

response = json.loads(r.read().decode('utf-8'))

distances = response['one_to_many'][0]

print("Stations, sorted by distance")
reverseDistances = sorted(distances[1:], key = lambda x: x['distance'])

for rd in reverseDistances:
   print("%6.2f - %s" % (rd['distance'], sunrailLocations[rd['to_index']].name))
