# Alex Nagel and Kyle Pullen

import sys
import os
import random

# from numpy import *
# import scipy as sp
# from pandas import *
# from rpy2.robjects.packages import importr
# import rpy2.robjects as ro
# import pandas.rpy.common as com

# import deck
d = range(2,15)
c = range(2,15)
h = range(2,15)
s = range(2,15)
Diamonds = 1
Clubs = 2
Hearts = 3
Spades = 4
deck = []

# General Variables
players = raw_input("Players: ")
players = int(players) - 1
players_hands = []
players_seven = []
my_hand = []
burn_cards = []
burn = 3
community_cards = []
community = 5
my_seven = []

# capture cards
cards = raw_input("My Cards: ")
cards = cards.split(" ")
card1 = list(cards[0])
card2 = list(cards[1])

# card cleanup
if str(card1[0]).lower() == 't':
	card1[0] = 10
if str(card1[0]).lower() == 'j':
	card1[0] = 11
if str(card1[0]).lower() == 'q':
	card1[0] = 12
if str(card1[0]).lower() == 'k':
	card1[0] = 13 
if str(card1[0]).lower() == 'a':
	card1[0] = 14

if str(card2[0]).lower() == 't':
	card2[0] = 10
if str(card2[0]).lower() == 'j':
	card2[0] = 11
if str(card2[0]).lower() == 'q':
	card2[0] = 12
if str(card2[0]).lower() == 'k':
	card2[0] = 13 
if str(card2[0]).lower() == 'a':
	card2[0] = 14

# remove cards from deck and change to int
if str(card1[1]).lower() == 'd':
	d.remove(int(card1[0]))
	card1[1] = Diamonds
if str(card1[1]).lower() == 'c':
	c.remove(int(card1[0]))
	card1[1] = Clubs
if str(card1[1]).lower() == 's':
	s.remove(int(card1[0]))
	card1[1] = Spades
if str(card1[1]).lower() == 'h':
	h.remove(int(card1[0]))
	card1[1] = Hearts

if str(card2[1]).lower() == 'd':
	d.remove(int(card2[0]))
	card2[1] = Diamonds
if str(card2[1]).lower() == 'c':
	c.remove(int(card2[0]))
	card2[1] = Clubs
if str(card2[1]).lower() == 's':
	s.remove(int(card2[0]))
	card2[1] = Spades
if str(card2[1]).lower() == 'h':
	h.remove(int(card2[0]))
	card2[1] = Hearts

card1[0] = int(card1[0])
card2[0] = int(card2[0])
my_hand.append([card1, card2])


for card in d:
	deck.append([card, Diamonds])
for card in c:
	deck.append([card, Clubs])
for card in h:
	deck.append([card, Hearts])
for card in s:
	deck.append([card, Spades])

# generate random hands every time
random.shuffle(deck)

for card in range(burn):
	burn_cards.append(deck[card])
	deck.remove(deck[card])

for card in range(community):
	community_cards.append(deck[card])
	deck.remove(deck[card])

for player in range(players):
	players_hands.append([deck[player], deck[player+1]])
	deck.remove(deck[player])
	deck.remove(deck[player+1])
	players_seven.append(players_hands[player] + community_cards)

my_seven = my_hand[0] + community_cards