import pygame
import sys
from pygame.locals import *
from config import *

def player_handle(player):
    key = pygame.key.get_pressed()
    
    if key[pygame.K_a]:
        player.move_ip(-PLAYER_SPEED, 0)
    elif key[pygame.K_d]:
        player.move_ip(PLAYER_SPEED, 0)
    
    if player[0] < 0:
        player[0] = 0
    if player[0] > DISPLAY_SIZE[0] - PLAYER[3]: 
        player[0] = DISPLAY_SIZE[0] - PLAYER[3]
    
    if key[pygame.K_SPACE]:
        print("SPACE PRESSED")
        player_shoot()

def player_shoot():
    pass

def enemy_handle():
    pygame.draw.circle(color="blue")