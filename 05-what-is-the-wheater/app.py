from pgzero.builtins import Actor
import pygame, pgzrun
import json
from turtle import Screen


pygame.init()

WIDTH = 1536
HEIGHT = 1175

BLACK = (0,0,0)

map = pygame.image.load('singapore_map.png')
map = pygame.transform.scale(map, (WIDTH, HEIGHT))

def draw():
    print('drawing ...')
    screen.clear()
    screen.blit(map, (0, 0))
    coordinates = load_coordinates("area_coordinates.json")
    for area in coordinates:
        print(area)
        print(coordinates[area])
        x = coordinates[area][0]
        y = coordinates[area][1]
        print(x)
        print(y)
        screen.draw.text(str(area), color="black", topleft=(x, y))
    
def load_coordinates(json_file):
    with open(json_file, "r") as file:
        return json.load(file)


pgzrun.go()