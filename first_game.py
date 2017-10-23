# Import modules
import pygame
from pygame.locals import *

# The program's "main" function
def main():
	# Initialize modules
	pygame.init()

	# Declare main variables
	width = 640 # Dimensions of the display
	height = 480
	background_color = (255, 255, 255) # RGB color tuple (0 - 255)

	# Setup display
	# display.set_mode(dimentions_tuple, flags=0, color_depth)
	displaySurface = pygame.display.set_mode((width, height), 0, 32)
	pygame.display.set_caption("My first game!")

	# Internal "game clock"
	clock = pygame.time.Clock()

	# Main loop
	while True:
		# Color the display with the chosen background color
		displaySurface.fill(background_color)

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

		# Update the display everytime it changes
		pygame.display.update()

		# 60 FPS framerate cap
		clock.tick(60)

# Calling main()
main()
