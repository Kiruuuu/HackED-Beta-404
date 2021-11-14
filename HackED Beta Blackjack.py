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

#filetype = ".png"

img = []

for suit in suits:
	ace_card = "a" + "_" + suit
	cards.append(ace_card)
	for card_num in range (2, 11):
		card = str(card_num) + "_" + suit
		cards.append(card)
	for royal in royalty:
		card = str(royal) + "_" + suit
		cards.append(card)


def card_deal():
	p_card1 = None
	p_card2 = None
	d_card1 = None
	d_card2 = None
	while (p_card1 == p_card2) or (p_card1 == d_card1) or\
		(p_card1 == d_card2) or (p_card2 == d_card1) or\
		(p_card2 == d_card2) or (d_card1 == d_card2):
		p_card1 = rnd.randint(0,51)
		p_card2 = rnd.randint(0,51)
		d_card1 = rnd.randint(0,51)
		d_card2 = rnd.randint(0,51)
	return [p_card1, p_card2, d_card1, d_card2]


def card_img():
	dealt_cards = card_deal()
	print(dealt_cards)
	# Changing from card index values to actual cards
	dealt_cards[0] = cards[dealt_cards[0]]
	dealt_cards[1] = cards[dealt_cards[1]]
	dealt_cards[2] = cards[dealt_cards[2]]
	dealt_cards[3] = cards[dealt_cards[3]]

	for card in range(len(dealt_cards)):
		img.append("cards/" + dealt_cards[card] + ".png")
	p_card1_img_call = img[0]
	p_card2_img_call = img[1]
	d_card1_img_call = img[2]
	d_card2_img_call = img[3]

	p_card1_img = pg.image.load(p_card1_img_call)
	p_card2_img = pg.image.load(p_card2_img_call)
	d_card1_img = pg.image.load(d_card1_img_call)
	d_card2_img = pg.image.load(d_card2_img_call)

	return p_card1_img, p_card2_img, d_card1_img, d_card2_img

p_card1_img, p_card2_img, d_card1_img, d_card2_img = card_img()

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
	
	window.blit(p_card1_img, (0,575))
	window.blit(p_card2_img, (225,575))
	pg.display.update()
	timer.tick(fps)

