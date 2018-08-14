"""
@author: hogledd
@date: 10/08/18

Definitions:
- Ground Zero: last known location of target
- Available Transport: modes of travel known to target
- Speed of Transport: lookup of speeds against modes

- Search Radius: the radius in units of measure

Assumptions: over time the search radius extends out from ground zero

License:
DONE: Select open source license

Inputs:
DONE: location data from photo
TODO: location data from social media posts
TODO: available transport methods from input
TODO: transport networks (e.g. walk, run, bike, bus, car, train, plane)

Dependencies:
DONE: exif scraping framework (https://github.com/ianare/exif-py)
DONE: command line framework (https://github.com/pallets/click)
TODO: geotools framework (https://github.com/googlemaps/google-maps-services-python) #google-api-python-client

Transformations:
TODO: Weighting of input data confidence (i.e. scores)
TODO: Correlation of time and space
TODO: Decay algorithm for time and space
TODO: Bayesian pruning for resetting ground zero
TODO: Central tendency of multiple locations

Outputs:
TODO: search radius from ground zero
TODO: sentry locations around perimeter
TODO: candidate search locations scored

Future Improvements:
TODO: predictive agent based modeling
TODO: extend application to use geographic networks
TODO: extend to consider virtual (i.e. social media) search patterns

"""

import datetime
import click
import utils
import scrape

@click.command()
@click.option('--source', prompt='url > ', help='The image URL you wish to scrape for EXIF GPS Coordinates.')
@click.option('--transport', prompt='transport > ', help='The target\'s mode of transport at time of photo.')
def main(source, transport):
    coords = scrape_coords(source)
    transport_speed = lookup_speed(transport)
    time_zero = scrape_time(source)

    current_time = datetime.datetime.now()
    time_delta = current_time - time_zero

    radius = transport_speed * time_delta
    area = (radius * 3.14)^2

    # a = pi r 2
    # p = 2 pi r

    print('Ground zero of target is at > ')
    print('With time zero at > ')
    print('The search radius is > ')
    print('The search area is > ')
    print('Establish a perimeter at > ')

    print('Additional evidence suggests widening (changing) the search area to > ')


def scrape_coords(URL):
    # check for valid URL
    if utils.check_valid_URL(URL) == True:
        # check if valid image
        # pull EXIF data
        return scrape.get_image_coords(url)
        # check for valid coordinates
        # return coordinates
    else:
        error_code = 'Invalid URL'
        return error_code
    print(URL)


def lookup_speed(mode):
    # check for valid mode
    # lookup speed
    # check for valid speed
    # return speed
    return 20
    print(mode)


if __name__ == '__main__':
    main()
