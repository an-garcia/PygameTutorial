#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2008/02/19/pygame-tutorial-7-more-on-lines/
# Drawing Lines part2

import pygame


# Draw corner lines
def draw_corner_lines():
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    running = True
    size = 250
    step = 10
 
    for x in range(0, size+1, step):
        pygame.draw.line(screen, (255, 255, 255), (0, 250-x), (x, 0))
 
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick()


# Draw corner lines in 4 corners
def draw_in_all_corner_lines():
    w = h = 500
    screen = pygame.display.set_mode((w+1, h+1))
    clock = pygame.time.Clock()
    running = True
    size = 250
    step = 10
    color = 255, 255, 255
     
    for x in range(0, size+1, step):
        pygame.draw.line(screen, color, (0, size-x), (x, 0))
        pygame.draw.line(screen, color, (w - (size-x), 0), (w, x))
        pygame.draw.line(screen, color, (w, h - (size-x)), (w-x, h))
        pygame.draw.line(screen, color, (250-x, h), (0, h-x))
 
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick()


# Animated draw corner lines in 4 corner lines.
def animate_draw_in_all_corner_lines():
    w = h = 500
    size = 250
    step = 10
    lines = []
    pos = 0
    maxlines = 40
 
    for x in range(0, size+1, step):
        lines.append((0, size-x, x, 0))

    for x in range(0, size+1, step):
        lines.append((w - (size-x), 0, w, x))

    for x in range(0, size+1, step):
        lines.append((w, h - (size-x), w-x, h))

    for x in range(0, size+1, step):
        lines.append((size-x, h, 0, h-x))

    screen = pygame.display.set_mode((w+1, h+1))
    clock = pygame.time.Clock()
    running = True
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        col = 0
        cur = pos

        for i in range(maxlines):
            x1, y1, x2, y2 = lines[cur]
            pygame.draw.line(screen, (col, col, col), (x1, y1), (x2, y2))

            cur += 1
            if cur >= len(lines): cur = 0
            col += 240 / maxlines

        pos += 1
        if pos >= len(lines): pos = 0
        pygame.display.flip()
        clock.tick(40)



# Main section
pygame.init()
#draw_corner_lines()
#draw_in_all_corner_lines()
animate_draw_in_all_corner_lines()
pygame.quit()
