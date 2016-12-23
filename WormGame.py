#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2008/03/01/pygame-tutorial-9-first-improvements-to-the-game/
# Draws a worm on screen that moves with direction keys.

import pygame
import random

class Worm:
    """ A worm. """
    
    def __init__(self, surface):
        self.surface = surface
        self.x = int(surface.get_width() / 2)
        self.y = int(surface.get_height() / 2)
        self.length = 1
        self.grow_to = 50
        self.vx = 0
        self.vy = -1
        self.body = []
        self.crashed = False
        self.color = 255, 255, 0

    def eat(self):
        self.grow_to += 25
 
    def event(self, event):
        """ Handle keyboard events. """
        if event.key == pygame.K_UP:
            self.vx = 0
            self.vy = -1
        elif event.key == pygame.K_DOWN:
            if self.vy == -1: return
            self.vx = 0
            self.vy = 1
        elif event.key == pygame.K_LEFT:
            if self.vx == 1: return
            self.vx = -1
            self.vy = 0
        elif event.key == pygame.K_RIGHT:
            if self.vx == -1: return
            self.vx = 1
            self.vy = 0

    def move(self):
        """ Move the worm. """
        self.x += self.vx
        self.y += self.vy

        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))

        if (self.grow_to > self.length):
            self.length += 1

        if len(self.body) > self.length:
            self.body.pop()
 
    def draw(self):
        #for x, y in self.body:
        #    self.surface.set_at((x, y), self.color)
        x, y = self.body[0]
        self.surface.set_at((x, y), self.color)
        x, y = self.body[-1]
        self.surface.set_at((x, y), (0, 0, 0))



class Food:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, surface.get_width())
        self.y = random.randint(0, surface.get_height())
        self.color = 255, 255, 255
 
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, 3, 3), 0)

    def erase(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, 3, 3), 0)

    def check(self, x, y):
        if x < self.x or x > self.x + 3:
            return False
        elif y < self.y or y > self.y + 3:
            return False
        else:
            return True



# Draws a worm
def worm_game():
    w = 500
    h = 500

    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()

    pygame.mixer.init()
    chomp = pygame.mixer.Sound("croc_chomp_x.wav")
    pygame.display.set_caption("Worm Game")

    score = 0
    worm = Worm(screen)
    food = Food(screen)
    running = True
 
    while running:
        #screen.fill((0, 0, 0))
        worm.move()
        worm.draw()
        food.draw()

        if worm.crashed:
            running = False
        elif worm.x <= 0 or worm.x >= w - 1:
            running = False
        elif worm.y <= 0 or worm.y >= h - 1:
            running = False
        elif food.check(worm.x, worm.y):
            score += 1
            worm.eat()
            chomp.play()
            print ("Score: ", score)
            food.erase()
            food = Food(screen)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                worm.event(event)

        pygame.display.flip()
        clock.tick(240)



# Main section
pygame.init()
worm_game()
pygame.quit()
