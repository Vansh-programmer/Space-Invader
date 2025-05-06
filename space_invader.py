import pygame
import os
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invader Game')
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# player
playerX = 400
playerY = 300
playerimg = pygame.image.load('player.png')
playerChange = 0


def player(x, y):
    screen.blit(playerimg, (playerX, playerY))


running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 0.5
        if event.key == pygame.K_RIGHT:
            playerX += 0.5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print('Key is released')
            playerChange = 0



    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()
