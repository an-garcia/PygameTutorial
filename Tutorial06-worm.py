#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2007/12/18/pygame-tutorial-6-from-pixel-to-worm/
# Draws a worm on screen that moves with direction keys.

import pygame

class Worm:
    """ A worm. """
 
    def __init__(self, surface, x, y, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = -1
        self.length = length
        self.body = []
        self.last = (0, 0)
        self.crashed = False

    def key_event(self, event):
        """ Handle key events that affect the worm. """
        if event.key == pygame.K_UP:
            self.dx = 0
            self.dy = -1
        elif event.key == pygame.K_DOWN:
            self.dx = 0
            self.dy = 1
        elif event.key == pygame.K_LEFT:
            self.dx = -1
            self.dy = 0
        elif event.key == pygame.K_RIGHT:
            self.dx = 1
            self.dy = 0

    def move(self):
        """ Move the worm. """
        self.body.insert(0, (self.x, self.y))
        self.x += self.dx
        self.y += self.dy

        r, g, b, a = self.surface.get_at((self.x, self.y))
        if (r, g, b) != (0, 0, 0):
            self.crashed = True
        
        if len(self.body) >= self.length:
            self.last = self.body.pop()
        else:
            self.last = self.body[-1]
  
    def draw(self):
        """ Draw the worm. """
        self.surface.set_at((self.x, self.y), (255, 255, 255))
        self.surface.set_at(self.last, (0, 0, 0))


# Draws a worm
def worm_game01():
    # Dimensions.
    width = 640 
    height = 400

    screen = pygame.display.set_mode((width, height))
    screen.fill((0, 0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    running = True
 
    # Our worm.
    w = Worm(screen, int(width/2), int(height/2), 200)

    while running:
        w.move()
        w.draw()

        if w.crashed or w.x <= 0 or w.x >= width-1 or w.y <= 0 or w.y >= height-1:
            print ("Crash!!!")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                w.key_event(event)
 
        pygame.display.flip()
        clock.tick(240)



# Main section
pygame.init()
worm_game01()
pygame.quit()
