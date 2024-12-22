"""
Shoot the Apple Game

This module implements a simple game where the player has to shoot an apple by
clicking on it.
The game keeps track of the score and the remaining time. The game ends when
the time is up.

Modules:
    random: Provides the randint function to generate random positions for the
    apple.
    pgzero.builtins: Provides the Actor class to create and manage game actors.
    pygame: Provides functionalities for initializing the game, playing
    background music, and handling events.
    pgzrun: Provides the main loop to run the game.

Functions:
    apple_position(): Prints the current position of the apple.
    draw(): Draws the game screen, including the apple, score, time left,
    and game over message if applicable.
    update(dt): Updates the game state by decrementing the time left.
    place_apple(): Places the apple at a random position within the
    game window.
    time_up(): Ends the game by setting the game_over flag to True
    and stopping the background music.
    on_mouse_down(pos): Handles the mouse down event to check
    if the apple is clicked and updates the score.

Constants:
    WIDTH (int): The width of the game window.
    HEIGHT (int): The height of the game window.
    SCORE (int): The player's score.
    GAME_OVER (bool): A flag indicating whether the game is over.
    TIME_LEFT (int): The remaining time for the game.
    TIME_UP (int): The initial time for the game.
    BLACK (tuple): The color black in RGB format.

Actors:
    apple: The apple actor that the player needs to click on.
"""

from random import randint
import pygame
import pgzrun
from pgzero.builtins import Actor


FILE = '04-shoot-the-apple/Cooking-Show-chosic.com_.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(FILE)
pygame.mixer.music.play()
pygame.event.wait()

WIDTH = 800
HEIGHT = 720
SCORE = 0
GAME_OVER = False
TIME_LEFT = 32
TIME_UP = 32
BLACK = (0,0,0)

apple = Actor('apple', topleft=(0,0))


def apple_position():
    """
    Prints the current position of the apple.

    This function prints the x and y coordinates of the apple object.
    """
    print(f'apple.x = {apple.x}')
    print(f'apple.y = {apple.y}')


def draw():
    """
    Draws the game screen, including the apple, score, time left, and game over
    message if applicable.

    This function performs the following tasks:
    - Clears the screen.
    - Draws the apple on the screen.
    - Displays the current score at the top left corner in green color.
    - Displays the remaining time at the top right corner in red color.
    - If the game is over, fills the screen with black and displays the final
    score in the center with turquoise and red colors.
    """
    screen.clear()
    apple.draw()
    screen.draw.text("Score: " + str(SCORE), color="green", topleft=(10, 10))
    screen.draw.text("TimeLeft:", color="red", topright=(764, 10))
    screen.draw.text(str(TIME_LEFT)[0:4], color="red", topleft=(766, 10))
    if GAME_OVER:
        screen.fill("black")
        screen.draw.text("Final Score: " + str(SCORE), centery=400,
                         centerx=409 , fontsize=60,
                         color="turquoise", gcolor="red")


def update(dt):
    """
    Update the game state by decrementing the time left.

    Args:
        dt (float): The amount of time to decrement from TIME_LEFT.

    This function checks if the game is over. If not, it decrements the
    TIME_LEFT
    by the given dt. If TIME_LEFT reaches zero or below, it calls the TIME_UP
    function
    to handle the end of the game.
    """
    global TIME_LEFT, GAME_OVER
    if not GAME_OVER:
        TIME_LEFT -= dt
        if TIME_LEFT <= 0:
            time_up()


def place_apple():
    """
    Places the apple at a random position within the game window.

    This function sets the x and y coordinates of the apple to random values
    within the bounds of the game window, ensuring the apple is fully visible.
    """
    apple.x = randint(51, WIDTH - apple.width)
    apple.y = randint(50, HEIGHT - apple.height)
    apple_position()


def time_up():
    """
    Ends the game by setting the game_over flag to True and stopping the
    background music.

    This function sets the global variable 'game_over' to True, indicating that
    the game has ended.
    It also stops any music that is currently playing using the pygame mixer.
    """
    global GAME_OVER
    GAME_OVER = True
    pygame.mixer.music.stop()


def on_mouse_down(pos):
    """
    Handles the mouse down event.

    This function is called when the mouse button is pressed. It checks if the
    click position collides with the apple. If it does, it increments the score
    and prints "Good shot!". Otherwise, it prints "You missed!". After checking
    the collision, it places the apple at a new position.

    Args:
        pos (tuple): The (x, y) position of the mouse click.
    """
    if apple.collidepoint(pos):
        print("Good shot!")
        global SCORE
        SCORE = SCORE + 1
    else:
        print("You missed!")

    place_apple()


clock.schedule(time_up, 32.0)
place_apple()
pgzrun.go()
