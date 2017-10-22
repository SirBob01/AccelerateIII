# Import modules
import pygame
from pygame.locals import *

# Initialize modules
pygame.init()

# Declare main variables
width = 1000 # Dimensions of the screen
height = 600
background_color = (0, 100, 0) # RGB color tuple (0 - 255)

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

	# Update the screen everytime it changes
	pygame.display.update()