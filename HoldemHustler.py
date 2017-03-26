# Alex Nagel and Kyle Pullen

import sys
import os

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

# capture cards
cards = raw_input("My Cards: ")
cards = cards.split(" ")
card1 = list(cards[0])
card2 = list(cards[1])

# card cleanup
if card1[0] == 't':
	card1[0] = 10
if card1[0] == 'j':
	card1[0] = 11
if card1[0] == 'q':
	card1[0] = 12
if card1[0] == 'k':
	card1[0] = 13 
if card1[0] == 'a':
	card1[0] = 14
	card1.append(1) 

if card2[0] == 't':
	card2[0] = 10
if card2[0] == 'j':
	card2[0] = 11
if card2[0] == 'q':
	card2[0] = 12
if card2[0] == 'k':
	card2[0] = 13 
if card2[0] == 'a':
	card2[0] = 14
	card2.append(1)

# remove cards from deck
if card1[1] == 'd':
	d.remove(int(card1[0]))
if card1[1] == 'c':
	c.remove(int(card1[0]))
if card1[1] == 's':
	s.remove(int(card1[0]))
if card1[1] == 'h':
	h.remove(int(card1[0]))

if card2[1] == 'd':
	d.remove(int(card2[0]))
if card2[1] == 'c':
	c.remove(int(card2[0]))
if card2[1] == 's':
	s.remove(int(card2[0]))
if card2[1] == 'h':
	h.remove(int(card2[0]))



