import os
import pygame
import button
from sys import exit

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 45)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Main Menu")
clock = pygame.time.Clock()

color = (0,0,0)
x = 200
y = 50
def draw_text(text,font, color, x,y):
    title = font.render(text,True,color)
    screen.blit(title,(x,y))

done = False

while not done:
    screen.fill((185, 217, 235))
    mouse_position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()

    draw_text("Dance Dance Revolution -- AOE Edition!",font,color,x,y)



    pygame.display.update()
    clock.tick(60)
