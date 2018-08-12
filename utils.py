"""
@author: hogledd
@date: 10/08/18

units of measure conversion (metric, imperial)
- km to miles
- miles to km

address geocoding
- address to geographic coordinates
- geographic coordinates to address

"""
import requests
#URL = 'https://www.instagram.com'
address = ''
lat = ''
lon = ''

def checkValidURL(URL):
    # use get request to check for status code 200
    r = requests.get(URL)
    if r.status_code == requests.codes.ok:
        return True
    else:
        return False
    # return URL
    print (URL)

def convertCoordsToAddress(lat,lon):
    # check for valid lat and lon
    # check for endpoint connection
    # use geoAPI to get address
    # return address
    print (address)

def convertAddressToCoords(address):
    # check for valid address
    # check for endpoint connection
    # use geoAPI to get coords
    # return lat, lon
    print (lat,lon)
