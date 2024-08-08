import os
import random
import pygame
from pygame.locals import *

from objects import World, Player, Button, draw_lines, load_level, draw_text, sounds

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
max_level = len(os.listdir('levels/'))
data = load_level(level)

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


# creating buttons
play= pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\play.png")
replay = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\replay.png")
home = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\home.png")
exit = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\exit.png")
setting = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\settings.png")


play_btn = Button(play, (128, 64), WIDTH//2 - WIDTH // 16, HEIGHT//2)
replay_btn  = Button(replay, (45,42), WIDTH//2 - 110, HEIGHT//2 + 20)
home_btn  = Button(home, (45,42), WIDTH//2 - 20, HEIGHT//2 + 20)
exit_btn  = Button(exit, (45,42), WIDTH//2 + 70, HEIGHT//2 + 20)


# function to reset a level
def reset_level(level):
	global cur_score
	cur_score = 0

	data = load_level(level)
	if data:
		for group in groups:
			group.empty()
		world = World(win, data, groups)
		player.reset(win, player_pos, world, groups)

	return world

score = 0
cur_score = 0

main_menu = True
game_over = False
level_won = False
game_won = False
running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	pressed_keys = pygame.key.get_pressed()

	# displaying background & sun image
	win.blit(bg, (0,0))
	win.blit(sun, (40,40))
	world.draw()
	for group in groups:
		group.draw(win)

	if main_menu:
		win.blit(jungle_dash, (WIDTH//2 - WIDTH//8, HEIGHT//4))

		play_game = play_btn.draw(win)
		if play_game:
			main_menu = False
			game_over = False
			game_won = False
			score = 0