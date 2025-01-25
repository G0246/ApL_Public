import pygame, sys
from pygame.locals import *
from config import *

class player(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def shoot(self):
        pygame.draw.circle(self, color="red", )