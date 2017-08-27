#!aladdin-env/bin/flask

# example:
#    http://127.0.0.1:5000/api/v1/closest_lynx?latitude=28.5675386&longitude=-81.3500532

from flask import Flask, request

import sys
import numpy as np
import pandas as pd
from scipy import spatial

df = pd.read_csv('LYNX_stop_coords.csv')
kd = spatial.KDTree(df[['Latitude', 'Longitude']])

app = Flask(__name__)

@app.route('/api/v1/closest_lynx', methods = ['GET'])
def closestLynx():
   latitude = request.args.get('latitude', 0)
   longitude = request.args.get('longitude', 0)
   searchResult = kd.query([float(latitude), float(longitude)])
   response = app.response_class(
        response = df.ix[searchResult[1]].to_json(),
        status = 200,
        mimetype = 'application/json'
   )
   return response

if __name__ == '__main__':
   app.run(debug = True)

