import time
import pygame
In=1
pygame.init()
w = 64
h = 32
size=(w,h)
screen = pygame.display.set_mode(size)
c = pygame.time.Clock() # create a clock object for timing

while True:
    img=pygame.image.load("tmp.png")
    screen.blit(img,(0,0))
    pygame.display.flip() # update the display
    In += 1