#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2007/12/09/pygame-tutorial-4-more-on-events/
# Deal with more mouse events.

import pygame


# Draw on the screen, but uses to much resources.
# Run the task manager and check CPU usage.
# This is because the poll() method returns an event of type NOEVENT if there
# is no event in the event queue. This is rather wasteful.
def draw_with_event_poll():
    screen = pygame.display.set_mode((640, 400))
    running = 1
  
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        else:
            print (event.type)


# A better way of writing our event loop.
# We will try out pygame.event.get() instead
def draw_with_event_get():
    screen = pygame.display.set_mode((640, 480))
    running = 1
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
            else:
                print (event.type)


# Have a clock that we use to regularly tell our pygame program to “take a rest”. 
def draw_with_sleep():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = 1
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
        clock.tick(20)


# Main section
pygame.init()
#draw_with_event_poll()
#draw_with_event_get()
draw_with_sleep()
pygame.quit()
