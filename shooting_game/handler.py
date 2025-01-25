import pygame
import random
from config import *

last_shot = 0

# Player handler (Beta)
def player_handle(player, bullets):
    global last_shot
    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_ip(-PLAYER_SPEED, 0)
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_ip(PLAYER_SPEED, 0)

    # Prevent leaving the screen
    if player[0] < 0:
        player[0] = 0
    if player[0] > DISPLAY_SIZE[0] - PLAYER[2]:
        player[0] = DISPLAY_SIZE[0] - PLAYER[2]

    # Handle shooting with cooldown
    if keys[pygame.K_SPACE]:
        current_time = pygame.time.get_ticks()
        if current_time - last_shot >= PLAYER_FIRE_COOLDOWN:
            last_shot = current_time
            player_shoot(player, bullets)

# Bullet spawner (Spawn at current location)
def player_shoot(player, bullets):
    bullet = pygame.Rect(player.centerx - BULLET_WIDTH // 2, player.top - BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT)
    bullets.append(bullet)

# Random enemy spawner
def enemy_handle(enemies):
    if random.randint(1, ENEMY_SPAWN_RATE) == 1:
        x = random.randint(ENEMY_RADIUS, DISPLAY_SIZE[0] - ENEMY_RADIUS)
        enemies.append([x, 0])