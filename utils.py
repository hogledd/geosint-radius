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


def main():
    URL = 'https://www.instagram.com'
    check_valid_URL(URL)
    address = ''
    lat = ''
    lon = ''


def check_valid_URL(URL):
    # use get request to check for status code 200
    r = requests.get(URL)
    if r.status_code == requests.codes.ok:
        return True
    else:
        return False
    # return URL
    print(URL)


def convert_coords_to_address(lat,lon):
    # check for valid lat and lon
    # check for endpoint connection
    # use geoAPI to get address
    # return address
    print(address)


def convert_address_to_coords(address):
    # check for valid address
    # check for endpoint connection
    # use geoAPI to get coords
    # return lat, lon
    print(lat,lon)


if __name__ == '__main__':
    main()