from argparse import Action
from re import S
from turtle import position
import pygame, random, itertools
from constants import *

class Deck:
    def __init__(self):
        self.cards = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
        'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',
        'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
        'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC']


    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

    

class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0
        self.cardcount = 0

    def deal_card(self, card):

        self.cards.append(card)
        self.cardcount +=1

    def card_string(self):
        return 'f'
        
    def calc_hand(self):

        ace =[]
        n_ace = []
        for i in self.cards:
            if 'A' not in i:
                n_ace.append(i)
            else:
                ace.append(i)


        for card in n_ace:
            if "K" in card:
                self.value += 10
            if "Q" in card:
                self.value += 10
            if "J" in card:
                self.value += 10
            if "10" in card:
                self.value += 10  
            if "9" in card:
                self.value += 9
            elif "8" in card:
                self.value += 8
            elif "7" in card:
                self.value += 7
            elif "6" in card:
                self.value += 6
            elif "5" in card:
                self.value += 5
            elif "4" in card:
                self.value += 4
            elif "3" in card:
                self.value += 3
            elif "2" in card:
                self.value += 2
            elif "1" in card:
                self.value += 1
        
        for card in ace:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1
        return self.value
    
    def display_cards(self):
        for card in self.cards:
            cards = "".join((card[0], card[1]))
            if card not in self.card_img:
                self.card_img.append(cards)
        
                

class Button():
    def __init__(self, image, x,y ):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    
    def draw(self,surface):
        action = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        

    def Input(self):
        pos = pygame.mouse.get_pos()
        # checks if x is in the range of the furthest left to right and if y is in the range of the furthest top and bottom 
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            action = True
        return action


        
    