

import pygame
import sys
import time
import pygbutton
from pygame.locals import *

#mode = input("Black or White? B/W")

pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (72, 93, 63)
RED = ( 255, 0, 0)

size = (488, 570)

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
                rect1 = pygame.draw.rect(screen, GREEN, (x * (size + 1), y * (size + 1), size, size))

        square_size = size+1

        def generate_buttons(x_pos, y_pos, size):
            field_buttons = []
            clicked_buttons = []
            for x in range(0, x_pos):
                button_row = []
                clicked_button_row = []
                for y in range(0, y_pos):
                    button_row.append(
                        pygbutton.PygButton((x * size, y * size, size, size), ""))
                    clicked_button_row.append(False)
                field_buttons.append(button_row)
                clicked_buttons.append(clicked_button_row)
            return [field_buttons, clicked_buttons]


        generated_buttons = generate_buttons(8, 8, size)
        field_buttons = generated_buttons[0]
        clicked_buttons = generated_buttons[1]

        squares_clicked = 0

        def draw_circle(x_pos,y_pos,col):

            x_pos = x_pos*size+x_pos
            y_pos = y_pos*size+y_pos
            pygame.draw.rect(screen, GREEN, [x_pos, y_pos, size, size])
            pygame.draw.ellipse(screen, col, (x_pos, y_pos, size, size))


        def start():
            for x in range(0, 8):
                for y in range(0, 8):
                    if x == 4 and y == 4:
                        a = 1
                    elif x == 3 and y == 4:
                        a = 1
                    elif x == 3 and y == 3:
                        a = 0
                    elif x == 4 and y == 3:
                        a = 0
                    else:
                        field_buttons[x][y].draw(screen)

            draw_circle(4, 4, BLACK)
            draw_circle(3, 3, BLACK)
            draw_circle(3, 4, WHITE)
            draw_circle(4, 3, WHITE)


        for x in range(0, 8):
            for y in range(0, 8):
                if clicked_buttons[y][x] is False:
                    field_buttons[y][x].draw(screen)


                        

        start()


        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()