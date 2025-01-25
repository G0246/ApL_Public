import pygame
import sys
from pygame.locals import *
from config import *
# from sprite import *

pygame.init()
pygame.display.set_caption("Simple Shooting Game")

screen = pygame.display.set_mode((DISPLAY_SIZE))
clock = pygame.time.Clock()
player = pygame.Rect(PLAYER)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1280, 720))
    pygame.draw.rect(screen, (255, 255 , 255), player)

    key = pygame.key.get_pressed()
    
    if key[pygame.K_a]:
        player.move_ip(-PLAYER_SPEED, 0)
    elif key[pygame.K_d]:
        player.move_ip(PLAYER_SPEED, 0)
    
    if player[0] < 0:
        player[0] = 0
    if player[0] > DISPLAY_SIZE[0] - PLAYER[0]: 
        player[0] = DISPLAY_SIZE[0] - PLAYER[0]
        
    pygame.display.update()
    clock.tick(60)

print("User initiated exit.")
pygame.quit()
sys.exit()