#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2007/12/16/pygame-tutorial-5-pixels/
# Plot individual pixels. We will also look at a keyboard event that may prove useful when we get to the stage of actually being able to write games.

import pygame
import random


# Plots random pixels
def random_pixels():
    # Window dimensions
    width = 640
    height = 400
 
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    while running:
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        screen.set_at((x, y), (red, green, blue))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(240)


# Moves a pixel along the screen.
# Using the cursor keys you can change the direction of the pixel.
# If the pixel hits any of the borders the program terminates
def move_pixel():
    # Window dimensions.
    width = 640
    height = 400

    # Position of the pixel.
    x = int(width / 2)
    y = int(height / 2)

    # Direction of the pixel.
    dir_x = 0
    dir_y = -1
 
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    while running:
        x += dir_x
        y += dir_y

        if x <= 0 or x >= width or y <= 0 or y >= height:
            print ("Crash!")
            running = False
            
        screen.fill((0, 0, 0))
        screen.set_at((x, y), (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dir_x = 0
                    dir_y = -1
                elif event.key == pygame.K_DOWN:
                    dir_x = 0
                    dir_y = 1
                elif event.key == pygame.K_LEFT:
                    dir_x = -1
                    dir_y = 0
                elif event.key == pygame.K_RIGHT:
                    dir_x = 1
                    dir_y = 0

        pygame.display.flip()
        clock.tick(120)



class MovingPixel:
    """ A moving pixel class. """

    def __init__(self, x, y):
        """ Creates a moving pixel. """
        self.x = x
        self.y = y
        self.hdir = 0
        self.vdir = -1

    def direction(self, dir):
        """ Changes the pixels direction. """
        self.hdir, self.vdir = dir

    def move(self):
        """ Moves the pixel. """
        self.x += self.hdir
        self.y += self.vdir

    def draw(self, surface):
        surface.set_at((self.x, self.y), (255, 255, 255))


# Move a single pixel around the screen without crashing against the borders.
def move_pixel_not_crash():
    # These are used for directions.
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    # Window dimensions.
    width = 640
    height = 400

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    # Create a moving pixel.
    pix = MovingPixel(int(width/2), int(height/2))

    while running:
        pix.move()

        if pix.x <= 0 or pix.x >= width or pix.y <= 0 or pix.y >= height:
            print ("Crash!")
            running = False

        screen.fill((0, 0, 0))
        pix.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pix.direction(UP)
                elif event.key == pygame.K_DOWN:
                    pix.direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    pix.direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    pix.direction(RIGHT)

        pygame.display.flip()
        clock.tick(120)



# Main section
pygame.init()
#random_pixels()
#move_pixel()
move_pixel_not_crash()
pygame.quit()

