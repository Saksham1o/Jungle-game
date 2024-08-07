import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pickle
import pygame
from pygame.locals import *
from pprint import pprint

if not os.path.exists('levels/'):
	os.mkdir('levels/')


SIZE = WIDTH , HEIGHT= 1000, 650
tile_size = 50


pygame.init()
clock = pygame.time.Clock()
fps = 30

cols = WIDTH // tile_size
rows = HEIGHT // tile_size
margin = 210

win_width = WIDTH + margin
win_height = HEIGHT

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Level Editor')


sun_img = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\sun.png")
bg_img = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\BG1.png")
bg_img = pygame.transform.scale(bg_img, (win_width - margin, HEIGHT))

# buttons
save_img = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\assets/save_btn.png")
load_img = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\assets/load_btn.png")
left_img = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\assets/left.png")
right_img = pygame.image.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\img\\assets/right.png")

# tiles
tiles = []
for t in sorted(os.listdir('tiles/'), key=lambda s: int(s[:-4])):
	tile = pygame.image.load('tiles/' + t)
	tiles.append(tile)



clicked = False
current_level = 1


WHITE = (255, 255, 255)
GREEN = (144, 201, 120)
BLUE = (30, 144, 255)

font = pygame.font.SysFont('Futura', 24)

# Empty world data
world_data = []
for r in range(rows):
	c = [0] * cols
	world_data.append(c)
	
def draw_text(text_, font, color, pos):
	text = font.render(text_, True, color)
	win.blit(text, pos)

def draw_lines():
	for row in range(rows+1):
		pygame.draw.line(win, WHITE, (0, tile_size*row), (WIDTH, tile_size*row), 2)
	for col in range(cols):
		pygame.draw.line(win, WHITE, (tile_size*col, 0), (tile_size*col, HEIGHT), 2)

def draw_world():
	for row in range(rows):
		for col in range(cols):
			index = world_data[row][col]
			if index > 0:
				if index in range(1,14) or index in (25,26):
					#dirt block
					img = pygame.transform.scale(tiles[index-1], (tile_size, tile_size))
					win.blit(img, (col * tile_size, row * tile_size))
				if index == 14:
					#bush blocks
					img = pygame.transform.scale(tiles[index-1], (tile_size, int(tile_size * 0.50)))
					win.blit(img, (col * tile_size, row * tile_size + tile_size // 2))