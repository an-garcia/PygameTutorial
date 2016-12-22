#! /usr/bin/env python
# Source https://lorenzod8n.wordpress.com/2007/05/25/pygame-tutorial-1-getting-started/
# Sample display of a Window using pygame 

import pygame

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill((0, 0, 0))
    pygame.display.flip()
        
