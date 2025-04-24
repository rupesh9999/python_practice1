import pygame

import sys

def run_game():
    #Initialiuze pygame
    pygame.init()


    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Character")

    #Define the background color (deep sky blue)
    bg_color = (0, 191, 255)

    # Character settings
    character_width = 50
    character_height = 50
    character_color = (0, 0, 0)
    character_speed = 5

    # Create the character
    character_x = 800 // 2 - character_width // 2
    character_y = 600 - character_height // 2
    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

    # create a clock to control frame rate
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Get keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_rect.x -= character_speed
        if keys[pygame.K_RIGHT]:
            character_rect.x += character_speed
        if keys[pygame.K_UP]:
            character_rect.y -= character_speed
        if keys[pygame.K_DOWN]:
            character_rect.y += character_speed

        # Boundary checking
        if character_rect.left < 0:
            character_rect.left = 0
        if character_rect.right > 800:
            character_rect.right = 800
        if character_rect.top < 0:
            character_rect.top = 0
        if character_rect.bottom > 600:
            character_rect.bottom = 600

        # Fill the screen with the background color
        screen.fill(bg_color)

        # Draw the character
        pygame.draw.rect(screen, character_color, character_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 fps
        clock.tick(60)

#start the game 
run_game()