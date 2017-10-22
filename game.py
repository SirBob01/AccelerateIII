# Import modules
import pygame
from pygame.locals import *

# Initialize modules
pygame.init()

# Declare main variables
width = 1000 # Dimensions of the screen
height = 600
background_color = (0, 255, 0) # RGB color tuple (0 - 255)

# Setup display
# display.set_mode(dimentions_tuple, flags=0, color_depth)
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("My First Game!")

# Main loop
while True:
	# Color the screen with the chosen background color
	screen.fill(background_color)

	# Handle "events"
	# Events are anything that relates to user input including
	# keyboard, mouse, and even quitting.
	for e in pygame.event.get():
		if e.type == QUIT:
			quit() # Quit the game when the user "quits" the app
		if e.type == KEYDOWN:
			if e.key == K_UP:
				background_color = (255, 0, 0) # Pressing the "up" key makes the background red
		if e.type == KEYUP:
			background_color = (255, 255, 0) # Releasing any key will make the background yellow
		if e.type == MOUSEBUTTONDOWN:
			background_color = (0, 255, 0) # Holding the mouse button down makes it green
		if e.type == MOUSEBUTTONUP:
			background_color = (0, 0, 255) # Releasing the mouse button makes it blue

	# Update the screen everytime it changes
	pygame.display.update()