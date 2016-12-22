#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2007/05/27/pygame-tutorial-2-drawing-lines/
# Drawing lines on surfaces.

import pygame


# Draws an X on the screen.
def draw_X():
    screen = pygame.display.set_mode((640, 480))
    running = 1
    
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
            
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (0, 0, 255), (0, 0), (639, 479))
        pygame.draw.aaline(screen, (0, 0, 255), (639, 0), (0, 479))
        pygame.display.flip()    


# Draw a line that jumps up and down
def draw_moving_lines():
    y = 0
    dir = 1
    running = 1
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    linecolor = 255, 0, 0
    bgcolor = 0, 0, 0

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0

        screen.fill(bgcolor)
        pygame.draw.line(screen, linecolor, (0, y), (width-1, y))
        y += dir
        if y == 0 or y == height-1:
            dir *= -1
        pygame.display.flip()

# Draw a single color bar.
def draw_color_bar():
    y = 0
    dir = 1
    running = 1
    barheight = 124
    screen = pygame.display.set_mode((800, 600));
 
    barcolor = []
    for i in range(1, 63):
        barcolor.append((0, 0, i*4))
    for i in range(1, 63):
        barcolor.append((0, 0, 255 - i*4))
     
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
     
        screen.fill((0, 0, 0))
        for i in range(0, barheight):
            pygame.draw.line(screen, barcolor[i], (0, y+i), (799, y+i))
     
        y += dir
        if y + barheight > 599 or y < 0:
            dir *= -1
     
        pygame.display.flip()


# Main section
#draw_X()
#draw_moving_lines()
draw_color_bar()

    
    
