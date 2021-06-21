import time
import pygame
from pygame.locals import *
import video

pygame.init()
width = 1000
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Legendary Goddess')
# images
title = pygame.image.load("abc.png")
button1 = pygame.image.load("online.png")
# icon
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
# intro
x = 0
y = 1000

running = True
while (running):
    screen.blit(title, (0, 0))
    screen.blit(button1, (100, 1000))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if button1.get_rect().collidepoint(x, y):
                video.video()
                time.sleep(10)
                pygame.quit()


# loop over, quite pygame
pygame.quit()
