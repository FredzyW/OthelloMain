
import pygame
import sys
import time
import pygbutton
from pygame.locals import *


pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (72, 93, 63)
RED = ( 255, 0, 0)

size = (515, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("OTHELLO")

carryOn = True

clock = pygame.time.Clock()


while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop

        screen.fill(BLACK)
        # The you can draw different shapes and lines or add text to your background stage.
        size = 60
        for y in range(0, 8):
            for x in range(0, 8):
                rect1 = pygame.draw.rect(screen, GREEN, (x * (size + 5), y * (size + 5), size, size))

        square_size = size+5


        def generate_buttons():
            buttons = []
            for x in range(0, 8):
                button_row = []
                for y in range(0, 8):
                    button_row.append(
                        pygbutton.PygButton((x * square_size, y * square_size, square_size, square_size), ""))
                buttons.append(button_row)
            return [buttons]

        buttons = generate_buttons()[0]

        for x in range(0, 8):
            for y in range(0, 8):
                if x == 4 and y == 4:
                    a = 1
                else:
                    buttons[y][x].draw(screen)
        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()