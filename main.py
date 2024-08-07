import os
import random
import pygame
from pygame.locals import *

SIZE = WIDTH , HEIGHT= 1000, 650
tile_size = 50

pygame.init()
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption('DASH')
clock = pygame.time.Clock()
FPS = 30


# Background img
bg1 = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\BG1.png")
bg2 = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\BG2.png")
bg = bg1
sun = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\sun.png")
jungle_dash = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\assets/jungle dash.png")
you_won = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\won.png")


# loading level 1
level = 1

player_pos = (10, 340)


# creating world & objects
water_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
forest_group = pygame.sprite.Group()
diamond_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
bridge_group = pygame.sprite.Group()
groups = [water_group, lava_group, forest_group, diamond_group, enemies_group, exit_group, platform_group,
			bridge_group]
