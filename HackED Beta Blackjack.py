import pygame as pg
import random as rnd
from pygame.locals import *

# Global variables for easy changes
screen_width =1200
screen_height = 900
timer = None
window = None
fps = 30
bg = pg.Color(0, 120, 0)

# creating list of all cards
suits = ["club", "dia", "heart", "spade"]
royalty = ["j", "q", "k"]
cards = []
img_call_list = []


for suit in suits:
	ace_card = "a" + "_" + suit
	cards.append(ace_card)
	for card_num in range (2, 11):
		card = str(card_num) + "_" + suit
		cards.append(card)
	for royal in royalty:
		card = str(royal) + "_" + suit
		cards.append(card)

class button():
	def __init__(self, color, x,y,width,height, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text

	def draw(self,win,outline=None):
		#Call this method to draw the button on the screen
		if outline:
			pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

		pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

		if self.text != '':
			font = pg.font.SysFont('comicsans', 60)
			text = font.render(self.text, 1, (0,0,0))
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def over(self,pos):
		#Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True

		return False

def card_deal():
	dealt_cards = [None] * 14
	loop_cond = True
	while loop_cond:
		for card in range(len(dealt_cards)):
			dealt_cards[card] = rnd.randint(0,51)
			for i in range(52):
				if dealt_cards.count(i) > 1:
					loop_cond = True
					break
				else:
					loop_cond = False


	return dealt_cards


def card_img():
	dealt_cards = card_deal()
	print(dealt_cards)
	# Changing from card index values to actual cards


	for card in range(len(dealt_cards)):
		dealt_cards[card] = cards[dealt_cards[card]]
		img_call_list.append("cards/" + dealt_cards[card] + ".png")
		img_call_list[card] = pg.image.load(img_call_list[card])

	print(img_call_list)

	return img_call_list

img_call_list = card_img()

# PyGame initialization
pg.init()
timer = pg.time.Clock()
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("HackED Beta Blackjack 404")

hit_button = button((0,255,0), 0, 0, 250, 100,'HIT')
# Game Loop
finish = False
while finish == False:
	window.fill(bg)
	hit_button.draw(window, (0,0,0))
	for event in pg.event.get():
		pos = pg.mouse.get_pos()
		if event.type == QUIT:
			finish = True
		if event.type == pg.MOUSEBUTTONDOWN:
			if hit_button.over(pos):
				continue
		if event.type == pg.MOUSEMOTION:
			if hit_button.over(pos):
				hit_button.color = (255,0,0)
			else:
				hit_button.color = (0,255,0)

	
	window.blit(img_call_list[0], (0,575))
	window.blit(img_call_list[1], (225,575))
	window.blit(img_call_list[2], (975,0))
	window.blit(img_call_list[3], (750,0))
	pg.display.update()
	timer.tick(fps)
    
