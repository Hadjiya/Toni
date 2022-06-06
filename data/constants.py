from optparse import Values
import pygame

background_color = (0,135,62)
black = (0,0,0)


Values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
Suits = ['C', 'S', 'H', 'D']

card_images_names = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',
'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC']