# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  def __init__(self, name, lat, lon):
    self.name = name 
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"Name: {self.name} | Lat: {self.lat}, Lon: {self.lon}"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

import csv

cities = []

def cityreader(cities=[]):

  with open('cities.csv') as csv_file:
    data = csv.reader(csv_file, delimiter = ',')
    for row in data:
      if row[0]  != 'city':

        city_name = row[0]
        latitude = row[3]
        longitude = row[4]

        city_instance = City(city_name, latitude, longitude)
        cities.append(city_instance)

  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# Get latitude and longitude values from the user

location1 = input("Enter in lat1,lon1: ")
location1 = location1.split(',')
location1 = [float(location1[0]), float(location1[1])]
location2  = input("Enter in lat2,lon2: ")
location2 = location2.split(',')
location2 = [float(location2[0]), float(location2[0])]


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  lat_list = []
  lon_list = []
  # find the greater of the two values for both latitude and longitude
  if lat1 > lat2:
    print("lat1 > lat2")
    lat_list.append(lat1)
    lat_list.append(lat2)
  else:
    print("lat2 > lat1")
    lat_list.append(lat2)
    lat_list.append(lat1)
  if lon1 > lon2:
    print("lon1 > lon2")
    lon_list.append(lon1)
    lon_list.append(lon2)
  else:
    print("lon2 > lon1")
    lon_list.append(lon2)
    lon_list.append(lon1)

  for city in cities:
    # Case str to float
    lat = float(city.lat)
    lon = float(city.lon)
    if lon >= lon_list[1] and lon <= lon_list[0]:
      if lat >= lat_list[1] and lat <= lat_list[0]:
          within.append(city)

  return within

print(cityreader_stretch(location1[0], location1[1], location2[0], location2[1], cities))