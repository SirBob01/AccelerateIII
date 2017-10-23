# Import modules
import random
import pygame
from pygame.locals import *

# Create game objects
class Player(object):
	def __init__(self, x, y):
		self.position = [x, y]
		self.dimensions = [50, 50]
		self.velocity = [0, 0]
		self.image = pygame.image.load("player.png").convert()

	def update(self):
		self.position[0] += self.velocity[0]
		self.position[1] += self.velocity[1]

	def draw(self, screen):
		screen.blit(self.image, self.position)


class Item(object):
	def __init__(self, x, y):
		self.position = [x, y]
		self.dimensions = [50, 50]
		self.image = pygame.image.load("item.png").convert()

	def draw(self, screen):
		screen.blit(self.image, self.position)

