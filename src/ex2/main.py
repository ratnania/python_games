import sys, pygame
import numpy as np
from numpy.random import random

pygame.init()

size = width, height = 1000, 800

amplitude_max = 4.
amplitude = amplitude_max * random()
speed = [amplitude*random(), amplitude*random()]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
done = False
is_blue = True
x = 30
y = 30

ball = pygame.image.load("../../images/owl_books.png")
ball = pygame.transform.scale(ball, (80, 60))
ballrect = ball.get_rect()

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN \
        and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((0,0,0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if ballrect.left < x and x < ballrect.right and ballrect.top < y and y < ballrect.bottom :
        # ... collapse : change velocity and color
        color = (255, 100, 0)
        amplitude = amplitude_max * random()
        speed = [amplitude*random(), amplitude*random()]
    else:
        color = (0, 128, 255)

    pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60))
    screen.blit(ball, ballrect)

    pygame.display.flip()
    clock.tick(60)
