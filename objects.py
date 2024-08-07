import os
import pickle
import random
import pygame
from pygame import mixer
from pygame.locals import *

SIZE = WIDTH , HEIGHT= 1000, 650
tile_size = 50

pygame.font.init()
score_font = pygame.font.SysFont('Bauhaus 93', 30)

WHITE = (255,255,255)
BLUE = (30, 144, 255)

mixer.init()

pygame.mixer.music.load("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\sounds\\Ballad for Olivia.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0, 5000)

diamond_fx = pygame.mixer.Sound("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\sounds\\sounds/341695__projectsu012__coins-1.wav")
diamond_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\sounds\\jump.wav")
jump_fx.set_volume(0.5)
dead_fx = pygame.mixer.Sound("C:\\Users\\Saksham\\Desktop\\git28\\Jungle-game\\sounds\\406113__daleonfire__dead.wav")
dead_fx.set_volume(0.5)
sounds = [diamond_fx, ]

# creates background
class World:
	def __init__(self, win, data, groups):
		self.tile_list  = []
		self.win = win
		self.groups = groups

		tiles = []
		for t in sorted(os.listdir('tiles/'), key=lambda s: int(s[:-4])):
			tile = pygame.image.load('tiles/' + t)
			tiles.append(tile)

		row_count = 0
		for row in data:
			col_count = 0
			for col in row:
				if col > 0:
					if col in range(1,14) or col == 18:
						# dirt blocks
						img = pygame.transform.scale(tiles[col-1], (tile_size, tile_size))
						rect = img.get_rect()
						rect.x = col_count * tile_size
						rect.y = row_count * tile_size
						tile = (img, rect)
						self.tile_list.append(tile)
