from pgzero.builtins import Actor
import pygame, pgzrun
from random import randint

screen_width = 1280
screen_height = 720

pygame.init()
screen1 = pygame.display.set_mode((screen_width,screen_height))

BLACK = (0,0,0)

apple = Actor('apple')

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()

    else:
        print("You missed!")
        quit()#If you want to add a Timer remenber to delete this.



pgzrun.go()