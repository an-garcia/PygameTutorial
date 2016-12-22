#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2007/05/30/pygame-tutorial-3-mouse-events/
# Deal with mouse events.

import pygame


# Tracks the position of the mouse on our window. 
def track_mouse_position():
    x = y = 0
    running = 1
    screen = pygame.display.set_mode((640, 400))

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEMOTION:
            print ("mouse at ", event.pos)

        screen.fill((0, 0, 0))
        pygame.display.flip()


# Draws lines that cut the mouse pointer’s coordinates.
def draw_lines_using_mouse_position():
    bgcolor = 0, 0, 0
    linecolor = 255, 255, 255
    x = y = 0
    running = 1
    screen = pygame.display.set_mode((640, 400))
     
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
    
        screen.fill(bgcolor)
        pygame.draw.line(screen, linecolor, (x, 0), (x, 399))
        pygame.draw.line(screen, linecolor, (0, y), (639, y))
        pygame.display.flip()


# Draws lines that cut the mouse pointer’s coordinates flashins.
def draw_lines_using_mouse_position_flashing():
    bgcolor = 0, 0, 0
    blueval = 0
    bluedir = 1
    x = y = 0
    running = 1
    screen = pygame.display.set_mode((640, 400))

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos

        screen.fill(bgcolor)
        pygame.draw.line(screen, (0, 0, blueval), (x, 0), (x, 399))
        pygame.draw.line(screen, (0, 0, blueval), (0, y), (639, y))
        blueval += bluedir
        if blueval == 255 or blueval == 0: bluedir *= -1
        pygame.display.flip()


# Shows the coordinates when clicking on the screen.
def mouse_button_event():
    LEFT = 1
  
    running = 1
    screen = pygame.display.set_mode((320, 200))
 
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print ("You pressed the left mouse button at ", event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            print ("You released the left mouse button at ", event.pos)

        screen.fill((0, 0, 0))
        pygame.display.flip()


# Main section
pygame.init()
#track_mouse_position()
#draw_lines_using_mouse_position()
#draw_lines_using_mouse_position_flashing()
mouse_button_event()
pygame.quit()
