from pgzero.builtins import Actor
import pygame, pgzrun
import json
from turtle import Screen
import requests

# URL of the API
API_URL = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"


def load_coordinates(json_file):
    with open(json_file, "r") as file:
        return json.load(file)
    
def fetch_weather_data():
   try:
      # Send an HTTP GET request to the API
      response = requests.get(API_URL)
      
      # Raise an exception if the request was unsuccessful
      response.raise_for_status()
      
      # Parse the JSON response
      data = response.json()
      #print("Weather data:", data)
      return data
   except requests.exceptions.RequestException as e:
      # Print an error message if something goes wrong
      print(f"Error fetching data: {e}")
      return None

# Call the function to fetch weather data
coordinates = load_coordinates("area_coordinates.json")
wheater_data = fetch_weather_data()
#print(f'{wheater_data["items"][0]["forecasts"]}')

for area in coordinates:
    for data in wheater_data["items"][0]["forecasts"]:
        if area == data["area"]:
            print(f'{data["area"]}: {data["forecast"]}')

pygame.init()

WIDTH = 1536
HEIGHT = 1175

BLACK = (0,0,0)

map = pygame.image.load('singapore_map.png')
map = pygame.transform.scale(map, (WIDTH, HEIGHT))

sun = pygame.image.load('images/sun.png')
sun.convert()
sun = pygame.transform.scale(sun, (128, 128))
rect = sun.get_rect()

def draw():
    print('drawing ...')
    screen.clear()
    screen.blit(map, (0, 0))
    screen.blit(sun, rect)
    coordinates = load_coordinates("area_coordinates.json")
    for area in coordinates:
        print(area)
        print(coordinates[area])
        x = coordinates[area][0]
        y = coordinates[area][1]
        print(x)
        print(y)
        for data in wheater_data["items"][0]["forecasts"]:
            if area == data["area"]:
                print(f'{data["area"]}: {data["forecast"]}')
                forecasts = data["forecast"]
                screen.draw.text( str(area) + ":" + str(forecasts), color="blue", topleft=(x, y))

pgzrun.go()