import pygame
import sys
from pygame.locals import *
from config import *
from handler import *

pygame.init()
pygame.display.set_caption("Simple Shooting Game")

screen = pygame.display.set_mode(size=(DISPLAY_SIZE))
clock = pygame.time.Clock()
player = pygame.Rect(PLAYER)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1280, 720))
    pygame.draw.rect(screen, (255, 255, 255), player)

    player_handle()

    pygame.display.update()
    clock.tick(60)

print("User initiated exit.")
pygame.quit()
sys.exit()