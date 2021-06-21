"""import matplotlib.pyplot as plt

# x axis values
x = [150, 450, 100]
# corresponding y axis values
y = [450, 100, 50]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
"""
from moviepy.editor import VideoFileClip
import pygame
import time
import os

pygame.init()


def video():
    icon = pygame.image.load("icon.jpg")
    pygame.display.set_icon(icon)

    pygame.display.set_caption('The Legendary Goddess')

    clip = VideoFileClip('video.mp4')
    clip.preview()
    clip.close()
    os.system('python battle.py')




