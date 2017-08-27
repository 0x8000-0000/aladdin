#!/usr/bin/env python3

# example:
#    ./get_coordinates_for_address.py 2806 Corrine Dr, Orlando, FL 32803

import sys
import json
import urllib.request
import urllib.parse

query = { 'text': ' '.join(sys.argv[1:]), 'api_key': 'mapzen-eDR41VF' }

url = "https://search.mapzen.com/v1/search?%s" % urllib.parse.urlencode(query)

print(url)

req = urllib.request.Request(url)
rsp = urllib.request.urlopen(req)

response = json.loads(rsp.read().decode('utf-8'))

#print(json.dumps(response, indent = 3, sort_keys = True))
#print(json.dumps(response['features'], indent = 3, sort_keys = True))

print(response['features'][0]['geometry']['coordinates'])
