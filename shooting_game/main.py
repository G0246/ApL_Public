# Simple shooting game made with pygame

import pygame
import random
from pygame.locals import *
from config import *
from handler import *

pygame.init()
pygame.display.set_caption("Simple Shooting Game")

screen = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
player = pygame.Rect(PLAYER)

# Game data
bullets = []
enemies = []
score = 0

running = True
game_over = False

# Game over screen
def show_game_over_screen(screen, final_score):
    text = pygame.font.Font(None, 50).render("GAME OVER", True, (255, 0, 0))
    score_text = pygame.font.Font(None, 50).render(f"Score: {final_score}", True, (255, 255, 255))
    subtext = pygame.font.Font(None, 30).render("Press R to restart or Q to quit", True, (255, 255, 255))

    # Using DISPLAY_SIZE for easier change in the future
    screen.fill((0, 0, 0))
    screen.blit(text, (DISPLAY_SIZE[0] // 2 - text.get_width() // 2, DISPLAY_SIZE[1] // 2 - 80))
    screen.blit(score_text, (DISPLAY_SIZE[0] // 2 - score_text.get_width() // 2, DISPLAY_SIZE[1] // 2 - 30))
    screen.blit(subtext, (DISPLAY_SIZE[0] // 2 - subtext.get_width() // 2, DISPLAY_SIZE[1] // 2 + 20))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False
        clock.tick(30)

# MAIN
while running:
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Handle player
        player_handle(player, bullets)
        # Handle enemies
        enemy_handle(enemies)

        # Handle bullets
        for bullet in bullets[:]:
            bullet.y -= 10
            if bullet.y < 0:
                bullets.remove(bullet)

        # Move and handle enemies
        for enemy in enemies[:]:
            enemy[1] += ENEMY_SPEED
            if pygame.Rect(enemy[0] - ENEMY_RADIUS, enemy[1] - ENEMY_RADIUS, ENEMY_RADIUS * 2, ENEMY_RADIUS * 2).colliderect(player):
                game_over = True
            if enemy[1] > DISPLAY_SIZE[1]:
                enemies.remove(enemy)

        # Collision detection (hit you lol)
        for i in range(len(bullets) - 1, -1, -1):
            bullet = bullets[i]
            for j in range(len(enemies) - 1, -1, -1):
                enemy = enemies[j]
                enemy_center = (enemy[0], enemy[1])
                bullet_center = (bullet.centerx, bullet.centery)

                # Calculate distance
                distance = ((bullet_center[0] - enemy_center[0]) ** 2 + (bullet_center[1] - enemy_center[1]) ** 2) ** 0.5

                if distance <= ENEMY_RADIUS:
                    bullets.pop(i)
                    enemies.pop(j)
                    score += 5
                    break

        # Draw player, bullets, and enemies
        pygame.draw.rect(screen, (255, 255, 255), player)
        for bullet in bullets:
            pygame.draw.rect(screen, (255, 0, 0), bullet)
        for enemy in enemies:
            pygame.draw.circle(screen, (0, 0, 255), (enemy[0], enemy[1]), ENEMY_RADIUS)

        # Score thingy
        score_text = pygame.font.Font(None, 36).render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)
    else:
        # Show screen
        if show_game_over_screen(screen, score):
            # Restart the game
            player = pygame.Rect(PLAYER)
            bullets.clear()
            enemies.clear()
            score = 0
            game_over = False
        else:
            running = False

print("User initiated exit.")
pygame.quit()