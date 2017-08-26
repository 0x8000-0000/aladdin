#!/bin/sh

set -x

ORIGIN=28.600574,-81.197851
DESTINATION=28.5392688,-81.386124
API_KEY=AIzaSyAjjCs5kWwxdwOhULDuvhVMzct-xZzZLtI

URL=https://maps.googleapis.com/maps/api/directions/json?origin=${ORIGIN}\&destination=${DESTINATION}\&key=${API_KEY}

curl ${URL}

