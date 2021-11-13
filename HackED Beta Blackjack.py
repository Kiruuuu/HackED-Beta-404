import pygame as pg
from pygame.locals import *

# Global variables for easy changes
screen_width =1200
screen_height = 900
timer = None
window = None
fps = 30
bg = pg.Color(0, 120, 0)

# PyGame initialization
pg.init()
timer = pg.time.Clock()
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("HackED Beta Blackjack 404")

# Game Loop
finish = False
while finish == False:
	window.fill(bg)
	for event in pg.event.get():
		if event.type == QUIT:
			finish = True
	pg.display.update()
	timer.tick(fps)