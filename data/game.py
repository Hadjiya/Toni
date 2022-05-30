import pygame, sys
from constants import *
from classes import *
pygame.init()

clock = pygame.time.Clock()
KEYDOWN = pygame.USEREVENT+1
pygame.time.set_timer(KEYDOWN,7000)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('BlackJack')
screen.fill(background_color)

title = pygame.image.load("resources\Menu\Bj.png")
play_img = pygame.image.load("resources\Menu\play.png")
quit_img = pygame.image.load("resources\Menu\Quit.png")
playern = pygame.image.load("resources\Menu\playern.png")

playb = Button(play_img, 171, 250)
quitb = Button(quit_img, 171, 420)

def main_menu():  # Начално меню
    run = True
    while run:
        clock.tick(60)
        screen.blit(title, (12, 64))
        pygame.display.flip()
        
        playb.draw(screen)
        quitb.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playb.Input():
                    numberp()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitb.Input():
                    pygame.quit



def numberp():
    run = True

    while run:
        clock.tick(60)
        screen.fill(background_color)
        screen.blit(playern, (72, 262))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                scenario_1()

        pygame.display.update()

def scenario_1():
    run = True
    clock.tick(60)

    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()

    for i in range(2):
        player.deal_card(deck.deal())
        dealer.deal_card(deck.deal())
    
    pvalue = player.calc_hand()
    dvalue = dealer.calc_hand()

    print("Player Hand")
    print(player.cards)
    print(player.value)
    
    print("Dealer Hand")
    print(dealer.cards)
    print(dealer.value)
    while run:
        screen.fill(background_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if player.value == 21 and player.cardcount == 2:
                print("BlackJack")
                run = False
            elif player.value <= 21:    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    player.deal_card(deck.deal())
                    player.calc_hand() 
                    player.value = player.value - pvalue
                    pvalue = player.value
                    print("Player Hand")
                    print(player.cards)
                    print(player.value) 
                    print("Dealer Hand")
                    print(dealer.cards)
                    print(dealer.value)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    if dealer.value < 17 :
                        dealer.deal_card(deck.deal())
                        dealer.calc_hand() 
                        dealer.value = dealer.value - dvalue
                        dvalue = dealer.value
                        print("Player Hand")
                        print(player.cards)
                        print(player.value) 
                        print("Dealer Hand")
                        print(dealer.cards)
                        print(dealer.value)
                    if dealer.value >= 17 :
                        if dealer.value > 21: 
                            print ("House Bust")
                            run = False
                        elif player.value > dealer.value:
                            print("player wins")
                            run = False
                        elif player.value == dealer.value:
                            print("Push")
                            run = False
                        else :
                            print("House wins")
                            run = False
            else :
                print("Bust")
                run = False
    
            
                   

        pygame.display.update()
    
    




main_menu()
