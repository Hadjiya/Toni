from argparse import Action
from turtle import position
import pygame, random, itertools
from constants import *


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        self.cards = list(itertools.product(Values, Suits))


    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

    

class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.cardcount = 0
        self.card_img = []
        self.value = 0


    def deal_card(self, card):
        self.cards.append(card)
        self.cardcount + 1


    def calc_hand(self):

        index = [a_card[0] for a_card in self.cards]
        n_ace = [i for i in  index if i != 'A' ]
        ace = [i for i in  index if i == 'A' ]
        
        
        for card in n_ace:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)
        
        for card in ace:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1
        return self.value
                
    


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

        
    