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

					if col == 14:
						# bush
						bush = Forest('bush',col_count * tile_size, row_count * tile_size + tile_size // 2)
						self.groups[2].add(bush)

					if col == 15:
						# lava
						lava = Fluid('lava_flow', col_count * tile_size, row_count * tile_size + tile_size // 2)
						self.groups[1].add(lava)
					if col == 16:
						lava = Fluid('lava_still', col_count * tile_size, row_count * tile_size)
						self.groups[1].add(lava)
					
					if col == 17:
						# diamond
						diamond = Diamond(col_count * tile_size, row_count * tile_size)
						self.groups[3].add(diamond)
					if col == 19:
						# water block
						water = Fluid('water_flow', col_count * tile_size, row_count * tile_size + tile_size // 2)
						self.groups[1].add(water)
					if col == 20:
						# water block
						water = Fluid('water_still', col_count * tile_size, row_count * tile_size)
						self.groups[1].add(water)
					if col == 21:
						# tree
						tree = Forest('tree', (col_count-1) * tile_size + 10, (row_count-2) * tile_size + 5)
						self.groups[2].add(tree)
					if col == 22:
						# mushroom
						mushroom = Forest('mushroom', col_count * tile_size, row_count * tile_size + tile_size // 4)
						self.groups[2].add(mushroom)
					if col == 23:
						# bee
						bee = Bee(col_count * tile_size, row_count * tile_size)
						self.groups[4].add(bee)
					if col == 24:
						#Gate blocks
						gate = ExitGate(col_count * tile_size - tile_size//4, row_count * tile_size - tile_size//4)
						self.groups[5].add(gate)
					if col == 25:
						#Side moving platform
						platform = MovingPlatform('side', col_count * tile_size, row_count * tile_size)
						self.groups[6].add(platform)
					if col == 26:
						#top moving platform
						platform = MovingPlatform('up', col_count * tile_size, row_count * tile_size)
						self.groups[6].add(platform)
					if col == 27:
						#flower
						flower = Forest('flower', (col_count) * tile_size, row_count * tile_size)
						self.groups[2].add(flower)
					if col == 28:
						# bridge
						bridge = Bridge((col_count-2) * tile_size + 10, row_count * tile_size + tile_size // 4)
						self.groups[7].add(bridge)
					if col == 29:
						#Slime
						slime = Slime(col_count * tile_size - 10, row_count * tile_size + tile_size // 4)
						self.groups[4].add(slime)

				col_count += 1
			row_count += 1

			diamond = Diamond((WIDTH//tile_size - 3) * tile_size, tile_size // 2)
			self.groups[3].add(diamond)

	def draw(self):
		for tile in self.tile_list:
			self.win.blit(tile[0], tile[1])

