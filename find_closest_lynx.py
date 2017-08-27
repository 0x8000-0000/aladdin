#!/usr/bin/env python3

# run as ./find_closest_lynx.py LYNX_stop_coords.csv 28.5675386 -81.3500532

import sys
import numpy as np
import pandas as pd
from scipy import spatial

df = pd.read_csv(sys.argv[1])

kd = spatial.KDTree(df[['Latitude', 'Longitude']])

result = kd.query([float(sys.argv[2]), float(sys.argv[3])])

print(df.ix[result[1]])
