from pgzero.builtins import Actor
import pygame, pgzrun
from random import randint

file = '04-shoot-the-apple/Cooking-Show-chosic.com_.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

screen_width = 800
screen_height = 720
score = 0
game_over = False

pygame.init()
screen1 = pygame.display.set_mode((screen_width,screen_height))

BLACK = (0,0,0)



apple = Actor('apple')

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Score: " + str(score), color="green", topleft=(10, 10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def update():
    pass

def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 600)

def time_up():
    global game_over
    game_over = True
    pygame.mixer.music.stop()


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        global score
        score = score + 1
    else:
        print("You missed!")

    place_apple()

clock.schedule(time_up, 7.0)
place_apple()
pgzrun.go()