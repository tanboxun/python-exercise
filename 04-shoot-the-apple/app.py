from pgzero.builtins import Actor
import pygame, pgzrun
from random import randint

file = '04-shoot-the-apple/Cooking-Show-chosic.com_.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

WIDTH = 800
HEIGHT = 720
score = 0
game_over = False
time_left = 20
time_up = 20

BLACK = (0,0,0)



apple = Actor('apple', topleft=(0,0))

def apple_position():
    print(f'apple.x = {apple.x}')
    print(f'apple.y = {apple.y}')

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Score: " + str(score), color="green", topleft=(10, 10))
    screen.draw.text("TimeLeft: " + str(time_left) , color="red", topright=(794, 20))
    if game_over:
        screen.fill("black")
        screen.draw.text("Final Score: " + str(score), centery=430 , centerx=409 , fontsize=60 ,
                          color="turquoise", gcolor="red") 

def update(dt):
    global time_left, game_over
    if not game_over:
        time_left -= dt
        if time_left <= 0:
            time_up()

def place_apple():
    apple.x = randint(51, WIDTH - apple.width)
    apple.y = randint(50, HEIGHT - apple.height)
    apple_position()

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

clock.schedule(time_up, 30.0)
place_apple()
pgzrun.go()