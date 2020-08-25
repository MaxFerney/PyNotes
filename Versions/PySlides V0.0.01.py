#Author: Max Ferney
#Date Created: 9.16.2015
#Date Modified: 9.16.2015
#Version: 0.0.01
#Description: Organize and take notes with PyNotes!

import time
import os
import pygame

pygame.init()

SIZE = (800, 500)
TITLE = "PySlides V0.0.01"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)
GREEN = (0, 255, 0)


done = False

while not done:
    
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Drawing Code
    ''' fill '''
    screen.fill(BLACK)

    ''' objects '''
    pygame.draw.rect(screen, WHITE, [0,0,50,50])
    font = pygame.font.Font(None, 30)
    text = font.render("Testing Text", True, WHITE)
    screen.blit(text, (0, 90))
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

    
pygame.quit()










            
