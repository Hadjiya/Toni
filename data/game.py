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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                scenario_2()

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
                if dealer.value < 17 :
                        while dealer.value < 17:
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
                elif dealer.value >= 17 :
                    if dealer.value > 21: 
                        print ("Blackjack")
                        run = False
                        scenario_1()
                    elif player.value > dealer.value:
                        print("Blackjack")
                        run = False
                        scenario_1()
                    elif player.value == dealer.value:
                        print("Push")
                        run = False
                        scenario_1()
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    while run:
                        if dealer.value < 17 :
                            while dealer.value < 17:
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
                        elif dealer.value >= 17 :
                            if dealer.value > 21: 
                                print ("House Bust")
                                run = False
                                scenario_1()
                            elif player.value > dealer.value:
                                print("player wins")
                                run = False
                                scenario_1()
                            elif player.value == dealer.value:
                                print("Push")
                                run = False
                                scenario_1()
                            else :
                                print("House wins")
                                run = False
                                scenario_1()
            else :
                print("Bust")
                run = False
                scenario_1()
    
    
                   

        pygame.display.update()
    
def scenario_2():
    run = True
    clock.tick(60)

    deck = Deck()
    deck.shuffle()
    player1 = Hand()
    player2 = Hand()
    dealer = Hand()

    for i in range(2):
        player1.deal_card(deck.deal())
        player2.deal_card(deck.deal())
        dealer.deal_card(deck.deal())
    
    pvalue1 = player1.calc_hand()
    pvalue2 = player2.calc_hand()
    dvalue = dealer.calc_hand()

    print("Player 1 Hand")
    print(player1.cards)
    print(player1.value)
    
    print("Player 2 Hand")
    print(player2.cards)
    print(player2.value)

    print("Dealer Hand")
    print(dealer.cards)
    print(dealer.value)

    while run:
        screen.fill(background_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #Player 1 turn
            if player1.value == 21 and player1.cardcount == 2:
                if player2.value == 21 and player2.cardcount == 2:
                    if dealer.value < 17 :
                        while dealer.value < 17:
                            dealer.deal_card(deck.deal())
                            dealer.calc_hand() 
                            dealer.value = dealer.value - dvalue
                            dvalue = dealer.value
                            
                            print("Player 1 Hand")
                            print(player1.cards)
                            print(player1.value) 

                            print("Player 2 Hand")
                            print(player2.cards)
                            print(player2.value)

                            print("Dealer Hand")
                            print(dealer.cards)
                            print(dealer.value)
                            scenario_2()
                    elif dealer.value >= 17 :
                        if dealer.value > 21: 
                            print ("Blackjack for Player 1 and Player 2")
                            run = False
                            scenario_2()
                        elif player1.value > dealer.value:
                            print("Blackjack for Player 1 and Player 2")
                            run = False
                            scenario_2()
                        elif player1.value == dealer.value:
                            print("Push")
                            run = False
                            scenario_2()
                else :
                    if player2.value <= 21:
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_1:
                                player2.deal_card(deck.deal())
                                player2.calc_hand() 
                                player2.value = player2.value - pvalue2
                                pvalue2 = player2.value
                                print("Player 2 Hand")
                                print(player2.cards)
                                print(player2.value)  
                            elif event.key == pygame.K_2:
                                if dealer.value < 17 :
                                    while dealer.value < 17:
                                        dealer.deal_card(deck.deal())
                                        dealer.calc_hand() 
                                        dealer.value = dealer.value - dvalue
                                        dvalue = dealer.value
                                elif dealer.value >= 17 :
                                    if dealer.value > 21: 
                                        print ("Player 1 and Player 2 wins")
                                        run = False
                                        scenario_2()
                                elif player2.value == dealer.value:
                                    print ("Player 2 Pushes and Player 1 wins")
                                    run = False
                                    scenario_2()
                                elif player2.value > dealer.value:
                                    print("Player 2 and Player 1 wins")
                                    run = False
                                    scenario_2()
                                
                                else :
                                    print("Player 1 wins and Player 2 Bust")
                                    run = False
                                    scenario_2()
            elif player1.value <= 21:
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_1:
                        player1.deal_card(deck.deal())
                        player1.calc_hand() 
                        player1.value = player1.value - pvalue1
                        pvalue1 = player1.value
                        print("Player 1 Hand")
                        print(player1.cards)
                        print(player1.value) 
                    elif event.key == pygame.K_2:
                        #Player 2 turn
                        if player2.value <= 21:
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                                player2.deal_card(deck.deal())
                                player2.calc_hand() 
                                player2.value = player2.value - pvalue2
                                pvalue2 = player2.value
                                print("Player 2 Hand")
                                print(player2.cards)
                                print(player2.value)  
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                                if dealer.value < 17 :
                                    while dealer.value < 17:
                                        dealer.deal_card(deck.deal())
                                        dealer.calc_hand() 
                                        dealer.value = dealer.value - dvalue
                                        dvalue = dealer.value
                                elif dealer.value >= 17 :
                                    if dealer.value > 21: 
                                        print ("House Bust")
                                        run = False
                                        scenario_2()

                                elif player1.value == dealer.value:
                                    if player2.value == dealer.value:
                                        print("Player 1 and Player 2 Push")
                                        run = False
                                        scenario_2()
                                    elif player2.value > dealer.value:
                                        print ("Player 1 Pushes and Player 2 wins")
                                        run = False
                                        scenario_2()
                                    elif player2.value < dealer.value:
                                        print("Player 1 Pushes and Player 2 loses")
                                        run = False
                                        scenario_2()
                                elif player2.value == dealer.value:
                                    if player1.value > dealer.value:
                                        print ("Player 2 Pushes and Player 1 wins")
                                        run = False
                                        scenario_2()
                                    elif player1.value < dealer.value:
                                        print ("Player 2 Pushes and Player 1 loses")
                                        run = False
                                        scenario_2()
                                elif player1.value > dealer.value:
                                    if player2.value > dealer.value:
                                        print("Player 1 and PLayer 2 win")
                                        run = False
                                        scenario_2()
                                    elif player2.value < dealer.value:
                                        print("player 1 wins and PLayer 2 loses")
                                        run = False
                                        scenario_2()
                                elif player2.value > dealer.value:
                                    print ("Player 2 wins and Player 1 loses")
                                    run = False
                                    scenario_2()
                                else :
                                    print("Player 1 and Player 2 Bust")
                                    run = False
                                    scenario_2()
            else :
                if player2.value <= 21:
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_1:
                                player2.deal_card(deck.deal())
                                player2.calc_hand() 
                                player2.value = player2.value - pvalue2
                                pvalue2 = player2.value
                                print("Player 2 Hand")
                                print(player2.cards)
                                print(player2.value)  
                            elif event.key == pygame.K_2:
                                if dealer.value < 17 :
                                    while dealer.value < 17:
                                        dealer.deal_card(deck.deal())
                                        dealer.calc_hand() 
                                        dealer.value = dealer.value - dvalue
                                        dvalue = dealer.value
                                elif dealer.value >= 17 :
                                    if dealer.value > 21: 
                                        print ("Player 1 and House Bust, Player 2 wins")
                                        run = False
                                        scenario_2()
                                elif player2.value == dealer.value:
                                    print ("Player 2 Pushes and Player 1 busts")
                                    run = False
                                    scenario_2()
                                elif player2.value > dealer.value:
                                    print("Player 2 wins and PLayer 1 loses")
                                    run = False
                                    scenario_2()
                                
                                else :
                                    print("Player 1 and Player 2 Bust")
                                    run = False
                                    scenario_2()            
                                
        pygame.display.update()



main_menu()
