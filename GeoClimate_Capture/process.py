# import request library to make HTTP requests, os for environment variables
import urllib.request as request, json, time
import os

# Get GEOCODE_KEY
geoCodeKey = os.environ.get('GEOCODE_KEY')

# Get DARKSKY_KEY
darkSkyKey = os.environ.get('DARKSKY_KEY')


def getGeoFromAddr(city):

    city = city.replace(' ', '+')
    geoCoordReq = "https://maps.googleapis.com/maps/api/geocode/json?address=" + city + "&key=" + geoCodeKey
    # print("%s" %(geoCoordReq))
    g = request.urlopen(geoCoordReq)
    raw_result = g.read().decode('utf-8')
    geoResult = json.loads(raw_result)
    #latitude = geoResult['results'][0]['geometry']['location']['lat']
    #longitude = geoResult['results'][0]['geometry']['location']['lng']
    #print ("Latitude of %s: %s, Longitude of %s: %s" % (city, latitude, city, longitude))
    return geoResult


def getWeatherFromCoords(coords, date):

    fileName = "https://api.darksky.net/forecast/" + darkSkyKey + "/" + str(coords[0]) + "," + str(coords[1]) + "," + str(date) + "T00:00:00"
    f = request.urlopen(fileName)
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)
    #summary = parsed_json['currently']['summary'] + " " + str(parsed_json['currently']['temperature'])
    #print ("Current summary in %s, %s, %s is: %s" % (city, state, country, summary))
    return parsed_json
