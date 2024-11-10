# Shoot the Apple - Assignment ReadMe

Welcome to the "Shoot the Apple" game assignment! In this assignment, you will create a simple game using Python and Pygame Zero where the goal is to shoot an apple that appears on the screen. This project will help you practice your coding skills and learn more about game development.

## Requirements
- Python 3.x installed on your computer
- Pygame Zero module installed (`pip install pgzero`)

## Objective
Create a game where:
- An apple appears at random positions on the screen.
- The player can shoot the apple by clicking on it.
- A score is displayed, which increases each time the apple is shot.
- The apple reappears in a new position after being clicked.

## Steps to Complete

1. **Setup Pygame Zero**
   - Create a new Python file (e.g., `shoot_the_apple.py`).
   - Import the Pygame Zero module by adding the following line at the top of your file:
     ```python
     import pgzrun
     ```

2. **Create the Game Window**
   - Set the size of the game window:
     ```python
     WIDTH = 800
     HEIGHT = 600
     ```

3. **Add the Apple Actor**
   - Create an `Actor` for the apple:
     ```python
     apple = Actor('apple')  # Make sure 'apple.png' is in the 'images' folder
     apple.pos = (400, 300)  # Initial position of the apple
     ```

4. **Randomize the Apple Position**
   - Use Python’s `random` module to move the apple to a new random position after it is clicked:
     ```python
     import random
     ```

5. **Draw the Apple and Score**
   - Create a function to draw the apple and display the score:
     ```python
     score = 0

     def draw():
         screen.clear()
         apple.draw()
         screen.draw.text(f"Score: {score}", (10, 10), color="white", fontsize=40)
     ```

6. **Detect Mouse Clicks**
   - Add an `on_mouse_down` function to check if the apple is clicked and update the score:
     ```python
     def on_mouse_down(pos):
         global score
         if apple.collidepoint(pos):
             score += 1
             apple.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
         else:
             print("You missed!")
     ```

7. **Run the Game**
   - Add the following line at the end of your script to start the game:
     ```python
     pgzrun.go()
     ```

## Tips
- Make sure the `images` folder contains `apple.png` to use as the apple image.
- Adjust the `WIDTH` and `HEIGHT` variables if you want to change the game window size.
- Feel free to add sound effects or improve the game by adding a timer or different levels.

## Challenges (Optional)
- Add a countdown timer to make the game more challenging.
- Display a "Game Over" message when time runs out.
- Add background music or sound effects when the apple is clicked.

## Have Fun!
Enjoy coding and playing your very own Python game! Happy learning!
