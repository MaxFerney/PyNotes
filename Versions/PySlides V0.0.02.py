#Author: Max Ferney
#Date Created: 9.16.2015
#Date Modified: 9.28.2015
#Version: 0.0.02
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


def DrawCursor(pos, shape='cross', color=GRAY, size=10):
    x = pos['x']
    y = pos['y']
    w = h = size/2
    #h = size/2
    def cross():
        pygame.draw.rect(screen, color, [x-5, +\
                                         y-1, +\
                                         size, +\
                                         2]) #y+((size/5)/2)
        
        pygame.draw.rect(screen, color, [x-1, +\
                                         y-5, +\
                                         2, +\
                                         size])#x+((size/5)/2) above line

    if shape=='cross':
        cross()

    else:
        cross()

#initial variables
box_pos01 = {'x': 0, 'y': 0}
box_pos02 = {'x': 0, 'y': 0}


# Game Loop
pygame.mouse.set_visible(0)
done = False
while not done:
    
    mousepos = pygame.mouse.get_pos()
    lstmousepos = {'x': mousepos[0], 'y': mousepos[1]}
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            box_pos01 = lstmousepos
        elif event.type == pygame.MOUSEBUTTONUP:
            box_pos02 = lstmousepos
        


    # Drawing Code
    ''' fill '''
    screen.fill(BLACK)

    ''' objects '''
    pygame.draw.rect(screen, WHITE, [0,0,50,50])
    font = pygame.font.Font(None, 30)
    text = font.render("Testing Text", True, WHITE)
    screen.blit(text, (0, 90))

    pygame.draw.rect(screen, WHITE, [box_pos01['x'],
                                     box_pos01['y'],
                                     box_pos02['x'] - box_pos01['x'],
                                     box_pos02['y'] - box_pos01['y']])
    


    #cursor
    DrawCursor(lstmousepos)
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

    
pygame.quit()










            
