from optparse import Values
import pygame

background_color = (0,135,62)
black = (0,0,0)


card_images_names = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','1H','JH','QH','KH',
'AD','2D','3D','4D','5D','6D','7D','8D','9D','1D','JD','QD','KD',
'AS','2S','3S','4S','5S','6S','7S','8S','9S','1S','JS','QS','KS',
'AC','2C','3C','4C','5C','6C','7C','8C','9C','1C','JC','QC','KC']


#rectangles for displaying cards wihtout updating the whole screen for 1 player mode

c_img_rect1 =  pygame.Rect((99,44), (140, 610))
c_img_rect2 =  pygame.Rect((99,44), (270, 610))
c_img_rect3  = pygame.Rect((99,44), (400, 610))
c_img_rect4 = pygame.Rect((99,44), (530, 610))
c_img_rect5 = pygame.Rect((99,44), (660, 610))
c_img_rectd1 = pygame.Rect((99,44), (140, 10))
c_img_rectlist1 = [c_img_rect1, c_img_rect2, c_img_rect3, c_img_rect4, c_img_rect5, c_img_rectd1]



#rectangles for displaying cards wihtout updating the whole screen for 2 player mode

#rect = (height,width),(x,y)
result_rect = pygame.Rect((200,1400),(0,300))

c_img_rect11 = pygame.Rect((99,44), (70, 610))
c_img_rect12 = pygame.Rect((99,44), (200, 610))
c_img_rect13 = pygame.Rect((99,44), (330, 610))
c_img_rect14 = pygame.Rect((99,44), (460, 610))
c_img_rect15 = pygame.Rect((99,44), (590, 610))

c_img_rect21 = pygame.Rect((99,44), (730, 610))
c_img_rect22 = pygame.Rect((99,44), (860, 610))
c_img_rect23 = pygame.Rect((99,44), (990, 610))
c_img_rect24 = pygame.Rect((99,44), (1120, 610))
c_img_rect25 = pygame.Rect((99,44), (1250, 610))

c_img_rect31 = pygame.Rect((99,44), (470, 10))
c_img_rect32 = pygame.Rect((99,44), (600, 10))
c_img_rect33 = pygame.Rect((99,44), (730, 10))
c_img_rect34 = pygame.Rect((99,44), (860, 10))
c_img_rect35 = pygame.Rect((99,44), (990, 10))
c_img_rectlist2 = [c_img_rect11, c_img_rect12, c_img_rect13, c_img_rect14, c_img_rect15, c_img_rect21
, c_img_rect22, c_img_rect23, c_img_rect24, c_img_rect25,c_img_rect31]