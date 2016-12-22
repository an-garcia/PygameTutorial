#! /usr/bin/env python

# Source https://lorenzod8n.wordpress.com/2007/05/27/pygame-tutorial-2-drawing-lines/
# Drawing lines on surfaces.


import pygame
from math import pi


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

# Draw sample objects
# Documentation http://www.pygame.org/docs/ref/draw.html
def sample_draw():
    # Initialize the game engine
    pygame.init()
     
    # Define the colors we will use in RGB format
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)
     
    # Set the height and width of the screen
    size = [400, 300]
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Example code for the draw module")
     
    #Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
     
    while not done:
     
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
         
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
     
        # All drawing code happens after the for loop and but
        # inside the main while done==False loop.
         
        # Clear the screen and set the screen background
        screen.fill(WHITE)
     
        # Draw on the screen a GREEN line from (0,0) to (50.75) 
        # 5 pixels wide.
        pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
     
        # Draw on the screen a GREEN line from (0,0) to (50.75) 
        # 5 pixels wide.
        pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
        
        # Draw on the screen a GREEN line from (0,0) to (50.75) 
        # 5 pixels wide.
        pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)

        # Draw a rectangle outline
        pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
         
        # Draw a solid rectangle
        pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
         
        # Draw an ellipse outline, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 

        # Draw an solid ellipse, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [300, 10, 50, 20]) 
     
        # This draws a triangle using the polygon command
        pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
      
        # Draw an arc as part of an ellipse. 
        # Use radians to determine what angle to draw.
        pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
        pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
        pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
        pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
        
        # Draw a circle
        pygame.draw.circle(screen, BLUE, [60, 250], 40)
        
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
     
    # Be IDLE friendly
    pygame.quit()



# Main section
#draw_X()
#draw_moving_lines()
#draw_color_bar()
sample_draw()
    
    
