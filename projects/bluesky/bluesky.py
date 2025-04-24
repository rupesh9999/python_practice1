import pygame

import sys

def run_game():
    # Initialize Pygame
    pygame.init()

    # set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blue Sky")

    # define the background clor (deep sky blue)
    bg_color = (0, 191, 255)

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # fill the screen with the background color
        screen.fill(bg_color)

        # Update the display
        pygame.display.flip()


# Start the game
run_game()