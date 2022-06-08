import pygame
import os
from constants import *
from classes import *
import time
pygame.init()

# For FPS
clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('BlackJack')
screen.fill(background_color)


# Loads images for every card
card_images = {}

for name in card_images_names:
    filename = 'E:\\Python\\PyGame\\Blackjack\\Sprites\\' + name + '.png'
    card_images[name] = pygame.image.load(filename).convert()

cardback = pygame.image.load(
    "E:\\Python\\PyGame\\Blackjack\\Sprites\\back.png").convert()

# Main Menu and text
title = pygame.image.load("Menu\Bj.png").convert()
play_img = pygame.image.load("Menu\play.png").convert()
quit_img = pygame.image.load("Menu\Quit.png").convert()
playern = pygame.image.load("Menu\playern.png").convert()

# ingame text
font1 = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 50)


def players(x, y, value):
    player = font1.render(str(value) , True, (0, 0, 0))
    screen.blit(player, (x, y))


def result(x, y, value):

    result = font2.render(str(value) , True, (0, 0, 0))
    screen.blit(result, (x, y))


# Score function
def show_score(x, y, value):
    score = font1.render('(' + str(value) + ')', True, (0, 0, 0))
    screen.blit(score, (x, y))


# Button creation
playb = Button(play_img, 171, 250)
quitb = Button(quit_img, 171, 420)


# Main Menu
def main_menu():
    run = True
    while run:
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


# Choosing number of players
def numberp():
    run = True
    while run:

        screen.fill(background_color)
        screen.blit(playern, (72, 262))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                scenario_1()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                scenario_2()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                run=False

        pygame.display.update()


def scenario_1():
    clock.tick(60)
    run = True
    stand = 0

    screen = pygame.display.set_mode((800, 800))
    
    #Creates the startup game state
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()

    for i in range(2):
        player.deal_card(deck.deal())
        dealer.deal_card(deck.deal())

    pvalue = player.calc_handp()
    dvalue = dealer.calc_handd()
    print (dealer.cards)
    while run:

        # displays background, score and text
        screen.fill(background_color)
        players(264, 550, "Player's Hand")
        show_score(510, 550, player.value)
        players(264, 200, "Dealer's Hand")

        # displays player's hand
        screen.blit(card_images[player.cards[0]], (140, 610))
        screen.blit(card_images[player.cards[1]], (270, 610))
        
        # displays dealer's hand
        screen.blit(card_images[dealer.cards[0]], (140, 10))
        if stand ==0:
            screen.blit(cardback, (270, 10))
        
        # game function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if player.value == 21 and player.cardcount == 2:
            #     if dealer.value < 17:
            #         while dealer.value < 17:
            #             dealer.deal_card(deck.deal())
            #             dealer.calc_hand()
            #             dealer.value = dealer.value - dvalue
            #             dvalue = dealer.value
            #             time.sleep(2)

            #     elif dealer.value >= 17:
            #         if dealer.value > 21:
            #             result(400, 400, "HOUSE BUST")
            #             time.sleep(3)
            #             run = False
            #             scenario_1()
            #         elif player.value > dealer.value:
            #             result(400, 400, "BLACKJACK")
            #             time.sleep(3)
            #             run = False
            #             scenario_1()
            #         elif player.value == dealer.value:
            #             result(400, 400, "PUSH")

            #             run = False
            #             scenario_1()
            elif player.value <= 21:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    pygame.time.delay(500)
                    player.deal_card(deck.deal())
                    player.calc_handp()
                    player.value = player.value - pvalue
                    pvalue = player.value
                    print(player.cards)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    stand += 1
                    while dealer.value < 17:
                        dealer.deal_card(deck.deal())
                        dealer.calc_handd()
                        dealer.value = dealer.value - dvalue
                        dvalue = dealer.value
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    pygame.quit
                    run = False
                
                #displays the rest of dealder's hand
                if stand == 1:
                    show_score(510, 200, dealer.value)
                    screen.blit(card_images[dealer.cards[1]], (270, 10))
                    pygame.display.update()
                    pygame.time.delay(1000)

                if dealer.cardcount >= 3:
                    screen.blit(card_images[dealer.cards[2]], (400, 10))
                    pygame.display.update()
                    pygame.time.delay(1000)

                if dealer.cardcount >= 4:
                    screen.blit(card_images[dealer.cards[3]], (530, 10))
                    pygame.display.update()
                    pygame.time.delay(1000)
                if dealer.cardcount >= 5:
                    screen.blit(card_images[dealer.cards[4]], (660, 10))
                    pygame.display.update()
                    pygame.time.delay(1000)
                
                #Displays the rest of player's hand
                if player.cardcount >= 3:
                    screen.blit(card_images[player.cards[2]], (400, 610))
                    pygame.display.update()
                if player.cardcount >= 4:
                    screen.blit(card_images[player.cards[3]], (530, 610))
                    pygame.display.update()
                if player.cardcount == 5:
                    screen.blit(card_images[player.cards[4]], (660, 610))
                    pygame.display.update()

                if dealer.value >= 17 and stand == 1:
                    if dealer.value > 21:
                        result(200, 400, "HOUSE BUST")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_1()
                    elif player.value > dealer.value:
                        result(200, 400, "PLAYER WINS")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_1()
                    elif player.value == dealer.value:
                        result(200, 400, "PUSH")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_1()
                    else:
                        result(200, 400, "HOUSE WINS")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_1()
        pygame.display.update()               
        if player.value > 21:
                result(200, 400, "PLAYER BUST")
                pygame.display.update()
                pygame.time.delay(3000)
                run = False
                scenario_1()
        



def scenario_2():
    #things the game needs to work
    clock.tick(60)
    run = True
    stand = 0
    player2turn = 0
    screen = pygame.display.set_mode((1400, 800))
    
    #Creates the startup game state
    deck = Deck()
    deck.shuffle()
    player1 = Hand()
    player2 = Hand()
    dealer = Hand()

    for i in range(2):
        player1.deal_card(deck.deal())
        player2.deal_card(deck.deal())
        dealer.deal_card(deck.deal())

    pvalue1 = player1.calc_handp()
    pvalue2 = player2.calc_handp()
    dvalue = dealer.calc_handd()

    print("Dealer Hand")
    print(dealer.cards)
    print(dealer.value)

    while run:

        # displays background, score and text
        screen.fill(background_color)
        players(200, 550, "Player 1's Hand")
        show_score(454, 550, player1.value)
        players(900,550,"Player 2's Hand")
        show_score(1154, 550, player2.value)
        players(570, 200, "Dealer's Hand")

        #Displays player 1 and 2's hand
        screen.blit(card_images[player1.cards[0]], (70, 610))
        screen.blit(card_images[player1.cards[1]], (200, 610))
        if player1.cardcount >= 3:
            screen.blit(card_images[player1.cards[2]], (330, 610))
            pygame.display.update(c_img_rect13)
        if player1.cardcount >= 4:
            screen.blit(card_images[player1.cards[3]], (460, 610))
            pygame.display.update(c_img_rect14)
        if player1.cardcount == 5:
            screen.blit(card_images[player1.cards[4]], (590, 610))
            pygame.display.update(c_img_rect15)

        screen.blit(card_images[player2.cards[0]], (730, 610))
        screen.blit(card_images[player2.cards[1]], (860, 610))
        if player2.cardcount >= 3:
            screen.blit(card_images[player2.cards[2]], (990, 610))
            pygame.display.update(c_img_rect23)
        if player2.cardcount >= 4:
            screen.blit(card_images[player2.cards[3]], (1120, 610))
            pygame.display.update(c_img_rect24)
        if player2.cardcount == 5:
            screen.blit(card_images[player2.cards[4]], (1250, 610))
            pygame.display.update(c_img_rect25)

        #Displays dealer's hand
        screen.blit(card_images[dealer.cards[0]], (470, 10))
        if stand == 0:
            screen.blit(cardback, (600, 10))
        #game function    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Player 1 turn
            # if player1.value == 21 and player1.cardcount == 2:
            #     if player2.value == 21 and player2.cardcount == 2:
            #         if dealer.value < 17:
            #             while dealer.value < 17:
            #                 dealer.deal_card(deck.deal())
            #                 dealer.calc_hand()
            #                 dealer.value = dealer.value - dvalue
            #                 dvalue = dealer.value

            #                 print("Player 1 Hand")
            #                 print(player1.cards)
            #                 print(player1.value)

            #                 print("Player 2 Hand")
            #                 print(player2.cards)
            #                 print(player2.value)

            #                 print("Dealer Hand")
            #                 print(dealer.cards)
            #                 print(dealer.value)
            #                 scenario_2()
            #         elif dealer.value >= 17:
            #             if dealer.value > 21:
            #                 print("Blackjack for Player 1 and Player 2")
            #                 run = False
            #                 scenario_2()
            #             elif player1.value > dealer.value:
            #                 print("Blackjack for Player 1 and Player 2")
            #                 run = False
            #                 scenario_2()
            #             elif player1.value == dealer.value:
            #                 print("Push")
            #                 run = False
            #                 scenario_2()
            #     else:
            #         if player2.value <= 21:
            #             if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            #                 player2.deal_card(deck.deal())
            #                 player2.calc_hand()
            #                 player2.value = player2.value - pvalue2
            #                 pvalue2 = player2.value
            #                 print("Player 2 Hand")
            #                 print(player2.cards)
            #                 print(player2.value)
            #             if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            #                 if dealer.value < 17:
            #                     while dealer.value < 17:
            #                         dealer.deal_card(deck.deal())
            #                         dealer.calc_hand()
            #                         dealer.value = dealer.value - dvalue
            #                         dvalue = dealer.value
            #                 elif dealer.value >= 17:
            #                     if dealer.value > 21:
            #                         print("Player 1 and Player 2 wins")
            #                         run = False
            #                         scenario_2()
            #                 elif player2.value == dealer.value:
            #                     print("Player 2 Pushes and Player 1 wins")
            #                     run = False
            #                     scenario_2()
            #                 elif player2.value > dealer.value:
            #                     print("Player 2 and Player 1 wins")
            #                     run = False
            #                     scenario_2()

            #                 else:
            #                     print("Player 1 wins and Player 2 Bust")
            #                     run = False
            #                     scenario_2()
            
            
            #player 1 turn
            if player1.value <=21 and player2turn == 0:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    pygame.time.delay(500)
                    player1.deal_card(deck.deal())
                    player1.value = player1.value - pvalue1
                    player1.calc_handp()
                    pvalue1 = player1.value

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    player2turn = 1

            elif player1.value > 21 and player2turn == 0:
                player2turn = 1
            
            # Player 2 turn 
            elif player2.value <= 21 and player2turn == 1:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    player2.deal_card(deck.deal())
                    player2.value = player2.value - pvalue2
                    player2.calc_handp()
                    pvalue2 = player2.value
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    stand = 1
                    print("down arrow")
                    while dealer.value < 17:
                        dealer.deal_card(deck.deal())
                        dealer.calc_handd()
                        dealer.value = dealer.value - dvalue
                        dvalue = dealer.value
                        print(dealer.cardcount)
                        print(dealer.cards)
                        print(dealer.value)
                    #Displays rest of dealer's hand and his score
                    show_score(510, 200, dealer.value)
                    screen.blit(card_images[dealer.cards[1]], (600, 10))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    
                    if dealer.cardcount >= 3:
                        screen.blit(card_images[dealer.cards[2]], (730, 10))
                        pygame.display.update(c_img_rect33)
                        pygame.time.delay(1000)

                    if dealer.cardcount >= 4:
                        screen.blit(card_images[dealer.cards[3]], (860, 10))
                        pygame.display.update(c_img_rect34)
                        pygame.time.delay(1000)
                    
                    if dealer.cardcount >= 5:
                        screen.blit(card_images[dealer.cards[4]], (990, 10))
                        pygame.display.update(c_img_rect35)
                        pygame.time.delay(1000)
                    
                    #checks who wins
                    if dealer.value > 21:
                        result(650, 400, "HOUSE BUST")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_2()
                    elif player1.value == dealer.value:
                        if player2.value == dealer.value:
                            result(650, 400, "Player 1 and Player 2 Push")
                            pygame.display.update()
                            pygame.time.delay(3000)
                            run = False
                            scenario_2()
                        elif player2.value > dealer.value:
                            result(650, 400, "Player 1 Push and Player 2 Wins")
                            pygame.display.update()
                            pygame.time.delay(3000)
                            run = False
                            scenario_2()
                        elif player2.value < dealer.value:
                            result(650, 400, "Player 1 Push and Player 2 Loses")
                            pygame.display.update()
                            pygame.time.delay(3000)
                            run = False
                            scenario_2()
                    elif player2.value == dealer.value:
                        if player1.value > dealer.value:
                            result(650, 400, "Player 1 Wins and Player 2 Push")
                            pygame.display.update()
                            pygame.time.delay(3000)
                            run = False
                            scenario_2()
                        elif player1.value < dealer.value:
                            result(650, 400, "Player 1 Loses and Player 2 Push")
                            pygame.display.update()
                            pygame.time.delay(3000)
                            run = False
                            scenario_2()
                    elif player1.value > dealer.value:
                        if player2.value > dealer.value:
                            result(650, 400, "Player 1 and Player 2 Win")
                            pygame.display.update()
                            pygame.time.delay(3000)
                            run = False
                            scenario_2()
                        elif player2.value < dealer.value:
                            result(650, 400, "Player 1 Wins and Player 2 Loses")
                            pygame.display.update()
                            pygame.time.delay(3000)
                            run = False
                            scenario_2()
                    elif player2.value > dealer.value:
                        result(650, 400, "Player 1 Loses and Player 2 Wins")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_2()
                    elif player2.value < dealer.value and player1.value < dealer.value:
                        result(650, 400, "Player 1 and Player 2 Lose")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_2()
                        
            elif player1.value > 21 and player2.value > 21:
                result(650, 400, "Player 1 and Player 2 Bust")
                pygame.display.update()
                pygame.time.delay(3000)
                run = False
                scenario_2()
            elif player2.value >21:
                while dealer.value < 17:
                    dealer.deal_card(deck.deal())
                    dealer.value = dealer.value - dvalue
                    dealer.calc_handd()
                    dvalue = dealer.value
                    print(dealer.cards)
                
                #Displays rest of dealer's hand and his score
                show_score(510, 200, dealer.value)
                screen.blit(card_images[dealer.cards[1]], (600, 10))
                pygame.display.update()
                pygame.time.delay(1000)
                
                if dealer.cardcount >= 3:
                    screen.blit(card_images[dealer.cards[2]], (730, 10))
                    pygame.display.update(c_img_rect33)
                    pygame.time.delay(1000)

                if dealer.cardcount >= 4:
                    screen.blit(card_images[dealer.cards[3]], (860, 10))
                    pygame.display.update(c_img_rect34)
                    pygame.time.delay(1000)
                
                if dealer.cardcount >= 5:
                    screen.blit(card_images[dealer.cards[4]], (990, 10))
                    pygame.display.update(c_img_rect35)
                    pygame.time.delay(1000)

                #Displays the result
                if dealer.value >= 17:
                    if dealer.value > 21:
                        result(650, 400, "Player 1 Wins and Player 2 Loses")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_2()
                elif player1.value == dealer.value:
                    result(650, 400, "Player 1 Push and Player 2 Bust")
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False
                    scenario_2()
                elif player1.value > dealer.value:
                    result(650, 400, "Player 1 Wins and Player 2 Bust")
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False
                    scenario_2()
                elif player2.value < dealer.value:
                        result(650, 400, "Player 1 Loses and Player 2 Bust")
                        pygame.display.update()
                        pygame.time.delay(3000)
                        run = False
                        scenario_2()
            else:
                result(650, 400, "Player 1 and Player 2 Bust")
                pygame.display.update()
                pygame.time.delay(3000)
                run = False
                scenario_2()

        pygame.display.update()


main_menu()
