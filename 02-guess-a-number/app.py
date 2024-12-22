"""
This script is a number guessing game where the user has to guess a randomly
generated number between 1 and 100.

The user has up to 10 attempts to guess the correct number. After each guess,
the script provides feedback indicating whether the guess was too low, too high,
or correct.

If the user guesses the correct number within 10 attempts, a congratulatory
message is displayed. If the user fails to guess the number within 10 attempts,
the script reveals the correct number.

Functions:
    None

Variables:
    number_i_think (int): The randomly generated number that the user has to
    guess.
    NUMBER_OF_GUESSES (int): The counter for the number of guesses made by the
    user.
"""
import random


number_i_think = random.randint(1, 100)
NUMBER_OF_GUESSES = 0

while NUMBER_OF_GUESSES < 10:
    print('Enter your guess:')
    guess = input()
    guess = int(guess)
    NUMBER_OF_GUESSES = NUMBER_OF_GUESSES + 1

    if guess < number_i_think:
        print('Too low')
    elif guess > number_i_think:
        print('Too high')
    elif guess == number_i_think:
        print('Congratulations! That is the number I was thinking of.')

    if NUMBER_OF_GUESSES >= 10:
        print(f'Aww you ran out of guesses.The  number I was thinking of was {number_i_think}')
