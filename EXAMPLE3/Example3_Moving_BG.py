import pygame
from pygame.locals import *
pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('EXEMPEL 3 - Rörlig bakgrund')
clock = pygame.time.Clock()
bg_img = pygame.image.load('Images/bg.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))
 
i = 0
 
runing = True
while runing:
    window.fill((0,0,0))
    window.blit(bg_img,(i,0))
    window.blit(bg_img,(width+i,0))
    if (i==-width):
        window.blit(bg_img,(width+i,0))
        i=0
    i-=1
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()