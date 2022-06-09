import pygame
import os
from pygame import mixer
from constants import *
from classes import *
#to prevent sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.init()
mixer.init()

FPS = 60
fpsClock = pygame.time.Clock()

#music that repeats forever
mixer.music.load("Menu\RegeanCalyp.mp3")
mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#apends text at the end of file
def winners(text_to_append):
    with open("E:\Python\PyGame\Blackjack\data\winners.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)
            


# Screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('BlackJack')
screen.fill(background_color)


# Using the dictionary from constants.py it loads image for every card by checking for identical names
card_images = {}
for name in card_images_names:
    filename = 'E:\\Python\\PyGame\\Blackjack\\Sprites\\' + name + '.png'
    card_images[name] = pygame.image.load(filename).convert()
cardback = pygame.image.load("E:\\Python\\PyGame\\Blackjack\\Sprites\\back.png").convert()

# Main Menu and text
title = pygame.image.load("Menu\Bj.png").convert()
play_img = pygame.image.load("Menu\play.png").convert()
quit_img = pygame.image.load("Menu\Quit.png").convert()
playern = pygame.image.load("Menu\playern.png").convert()


# ingame text fonts
font1 = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 50)

#function for displaying player's names on Window
def players(x, y, value):
    player = font1.render(str(value) , True, (0, 0, 0))
    screen.blit(player, (x, y))

#function for displaying the result of the round
def result(value):

    result = font2.render(str(value) , True, (0, 0, 0))
    result_rect = result.get_rect(center = pygame.display.get_surface().get_rect().center)
    screen.blit(result, result_rect)


# function to display the scores of players
def show_score(x, y, value):
    score = font1.render('(' + str(value) + ')', True, (0, 0, 0))
    screen.blit(score, (x, y))


# Creates buttons with the button class
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
    fpsClock.tick(FPS)
    run = True
    stand = 0
    bust = 0

    screen = pygame.display.set_mode((800, 800))
    
    #Creates the startup game state
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()

    for i in range(2):
        player.deal_card(deck.deal())
        dealer.deal_card(deck.deal())

    pvalue = player.calc_hand()
    dvalue = dealer.calc_hand()
   
    while run:

        # displays background, score and text
        screen.fill(background_color)
        players(264, 550, "Player's Hand")
        show_score(510, 550, player.value)
        players(264, 200, "Dealer's Hand")
    
        # displays player's hand
        screen.blit(card_images[player.cards[0]], (140, 610))
        screen.blit(card_images[player.cards[1]], (270, 610))
        
        if player.cardcount >= 3:
            screen.blit(card_images[player.cards[2]], (400, 610))
            if player.value > 21:
                bust = 1
        if player.cardcount >= 4:
            screen.blit(card_images[player.cards[3]], (530, 610))
            if player.value > 21:
                bust = 1
        if player.cardcount >= 5:
            screen.blit(card_images[player.cards[4]], (660, 610))
            if player.value > 21:
                bust = 1
        
        # displays dealer's hand
        screen.blit(card_images[dealer.cards[0]], (140, 10))
        if stand ==0:
            screen.blit(cardback, (270, 10))
            pygame.display.update(c_img_rectlist1) 
        
        # game function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #Blackjack situation
            if player.value == 21 and player.cardcount == 2:
        
                #displays dealder's hand
                show_score(510, 200, dealer.value)
                screen.blit(card_images[dealer.cards[1]], (270, 10))
                pygame.display.update()
                
                if dealer.value ==2 and dealer.cardcount == 2:
                    result("PUSH")
                    winners("PUSH")
                    pygame.display.update()
                    pygame.time.delay(4000)

                    run = False
                    scenario_1()
                else :
                    result("Blackjack")
                    winners("Blackjack")
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    scenario_1()

                
                
            #Player's turn
            elif player.value <= 21:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    pygame.time.delay(500)
                    player.deal_card(deck.deal())
                    player.value = player.value - pvalue
                    player.calc_hand()
                    pvalue = player.value

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    stand = 1
                    while dealer.value < 17:
                        dealer.deal_card(deck.deal())
                        dealer.value = dealer.value - dvalue
                        dealer.calc_hand()
                        dvalue = dealer.value
                
                #displays the rest of dealder's hand
                if stand == 1:
                    show_score(510, 200, dealer.value)
                    screen.blit(card_images[dealer.cards[1]], (270, 10))
                    pygame.display.update()
                    

                if dealer.cardcount >= 3:
                    screen.blit(card_images[dealer.cards[2]], (400, 10))
                    pygame.display.update()
                    

                if dealer.cardcount >= 4:
                    screen.blit(card_images[dealer.cards[3]], (530, 10))
                    pygame.display.update()
                    
                if dealer.cardcount >= 5:
                    screen.blit(card_images[dealer.cards[4]], (660, 10))
                    pygame.display.update()
                    
                
                if dealer.value >= 17 and stand == 1:
                    if dealer.value > 21:
                        result("HOUSE BUST")
                        winners("House Bust")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_1()
                    elif player.value > dealer.value:
                        result("PLAYER WINS")
                        winners("PLAYER WINS")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_1()
                    elif player.value == dealer.value:
                        result("PUSH")
                        winners("PUSH")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_1()
                    else:
                        result( "HOUSE WINS")
                        winners("HOUSE WINS")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_1()              
            if player.value > 21 and bust == 1:
                result("PLAYER BUST")
                winners("PLAYER BUST")
                pygame.display.update()
                pygame.time.delay(4000)
                run = False
                scenario_1()
        pygame.display.update()
        



def scenario_2():
    #things the game needs to work
    fpsClock.tick(FPS)
    
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

    pvalue1 = player1.calc_hand()
    pvalue2 = player2.calc_hand()
    dvalue = dealer.calc_hand()

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
            
        if player1.cardcount >= 4:
            screen.blit(card_images[player1.cards[3]], (460, 610))
            
        if player1.cardcount >= 5:
            screen.blit(card_images[player1.cards[4]], (590, 610))
            

        screen.blit(card_images[player2.cards[0]], (730, 610))
        screen.blit(card_images[player2.cards[1]], (860, 610))
        if player2.cardcount >= 3:
            screen.blit(card_images[player2.cards[2]], (990, 610))
            
        if player2.cardcount >= 4:
            screen.blit(card_images[player2.cards[3]], (1120, 610))
            
        if player2.cardcount >= 5:
            screen.blit(card_images[player2.cards[4]], (1250, 610))
            

        #Displays dealer's hand
        screen.blit(card_images[dealer.cards[0]], (470, 10))
        if stand == 0:
            screen.blit(cardback, (600, 10))
            pygame.display.update(c_img_rectlist2)

        #game function    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # Blackjack situation
            if player1.value == 21 and player1.cardcount == 2:
                if player2.value == 21 and player2.cardcount == 2:
                    while dealer.value < 17:
                        dealer.deal_card(deck.deal())
                        dealer.calc_hand()
                        dealer.value = dealer.value - dvalue
                        dvalue = dealer.value

                    #Displays rest of dealer's hand and his score
                    show_score(650, 250, dealer.value)
                    screen.blit(card_images[dealer.cards[1]], (600, 10))
                    pygame.display.update(c_img_rect32)
                    
                    
                    if dealer.cardcount >= 3:
                        screen.blit(card_images[dealer.cards[2]], (730, 10))
                        pygame.display.update(c_img_rect33)
                        

                    if dealer.cardcount >= 4:
                        screen.blit(card_images[dealer.cards[3]], (860, 10))
                        pygame.display.update(c_img_rect34)
                        
                    
                    if dealer.cardcount >= 5:
                        screen.blit(card_images[dealer.cards[4]], (990, 10))
                        pygame.display.update(c_img_rect35)
                        
                    
                    if dealer.value == 21 and dealer.cardcount == 2:
                        result("Push")
                        winners("Push")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_2()
                    else:
                        result("BLACKJACK")
                        winners("Blackjack")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_2()
                elif player2.value <= 21:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                            player2.deal_card(deck.deal())
                            player2.value = player2.value - pvalue2
                            player2.calc_hand()
                            pvalue2 = player2.value
                        
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                            while dealer.value < 17:
                                dealer.deal_card(deck.deal())
                                dealer.value = dealer.value - dvalue
                                dealer.calc_hand()
                                dvalue = dealer.value
                            
                            #Displays rest of dealer's hand and his score
                            show_score(650, 250, dealer.value)
                            screen.blit(card_images[dealer.cards[1]], (600, 10))
                            pygame.display.update(c_img_rect32)
                            
                            
                            if dealer.cardcount >= 3:
                                screen.blit(card_images[dealer.cards[2]], (730, 10))
                                pygame.display.update(c_img_rect33)
                                

                            if dealer.cardcount >= 4:
                                screen.blit(card_images[dealer.cards[3]], (860, 10))
                                pygame.display.update(c_img_rect34)
                                
                            
                            if dealer.cardcount >= 5:
                                screen.blit(card_images[dealer.cards[4]], (990, 10))
                                pygame.display.update(c_img_rect35)
                                
                            
                            if dealer.value > 21:
                                result("Player 1 Blackjack and Player 2 Wins")
                                winners("Player 1 Blackjack and Player 2 Wins")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()
                            elif dealer.value == 21 and dealer.cardcount ==2:
                                    result("Player 1 Push and Player 2 Loses")
                                    winners("Player 1 Push and Player 2 Loses")
                                    pygame.display.update()
                                    pygame.time.delay(4000)
                                    run = False
                                    scenario_2()
                            elif dealer.value == 21 :
                                if player2.value== 21:
                                    result("Player 1 Blackjack and Player 2 Push")
                                    winners("Player 1 Blackjack and Player 2 Push")
                                    pygame.display.update()
                                    pygame.time.delay(4000)
                                    run = False
                                    scenario_2()
                                else :
                                    result("Player 1 Blackjack and Player 2 Loses")
                                    winners("Player 1 Blackjack and Player 2 Loses")
                                    pygame.display.update()
                                    pygame.time.delay(4000)
                                    run = False
                                    scenario_2()
                            elif player2.value == dealer.value:
                                result("Player 1 Blackjack and Player 2 Pushes ")
                                winners("Player 1 Blackjack and Player 2 Pushes ")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()

                            elif player2.value > dealer.value:
                                result("Player 1 Blackjack and Player 2 Wins")
                                winners("Player 1 Blackjack and Player 2 Wins")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()

                            elif player2.value < dealer.value:
                                result("Player 1 Blackjack and Player 2 Loses")
                                winners("Player 1 Blackjack and Player 2 Loses")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()
                else :
                    result("Player 1 Blackjack and Player 2 Busts")
                    winners("Player 1 Blackjack and Player 2 Busts")
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    scenario_2()
            elif player2.value == 21 and player2.cardcount == 2:
                if player1.value <= 21:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                            player1.deal_card(deck.deal())
                            player1.value = player1.value - pvalue1
                            player1.calc_hand()
                            pvalue1 = player1.value
                        
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                            while dealer.value < 17:
                                dealer.deal_card(deck.deal())
                                dealer.value = dealer.value - dvalue
                                dealer.calc_hand()
                                dvalue = dealer.value
                            
                            #Displays rest of dealer's hand and his score
                            show_score(650, 250, dealer.value)
                            screen.blit(card_images[dealer.cards[1]], (600, 10))
                            pygame.display.update(c_img_rect32)
                            
                            
                            if dealer.cardcount >= 3:
                                screen.blit(card_images[dealer.cards[2]], (730, 10))
                                pygame.display.update(c_img_rect33)
                                

                            if dealer.cardcount >= 4:
                                screen.blit(card_images[dealer.cards[3]], (860, 10))
                                pygame.display.update(c_img_rect34)
                                
                            
                            if dealer.cardcount >= 5:
                                screen.blit(card_images[dealer.cards[4]], (990, 10))
                                pygame.display.update(c_img_rect35)
                                
                            
                            if dealer.value > 21:
                                result("Player 1 Blackjack and Player 2 Wins")
                                winners("Player 1 Blackjack and Player 2 Wins")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()
                            elif dealer.value == 21 and dealer.cardcount ==2:
                                result("Player 1 Loses and Player 2 Push")
                                winners("Player 1 Loses and Player 2 Push")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()
                            elif player1.value == dealer.value:
                                result("Player 1 Pushes and Player 2 Blackjack ")
                                winners("Player 1 Pushes and Player 2 Blackjack ")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()
                            elif player1.value > dealer.value:
                                result("Player 1 Wins and Player 2 Blackjack ")
                                winners("Player 1 Wins and Player 2 Blackjack ")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()
                            else:
                                result("Player 1 Loses and Player 2 Blackjack ")
                                winners("Player 1 Loses and Player 2 Blackjack ")
                                pygame.display.update()
                                pygame.time.delay(4000)
                                run = False
                                scenario_2()
                else:
                    result("Player 1 Busts and Player 2 Blackjack ")
                    winners("Player 1 Busts and Player 2 Blackjack ")
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    scenario_2()

            #player 1 turn
            elif player1.value <=21 and player2turn == 0:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    pygame.time.delay(500)
                    player1.deal_card(deck.deal())
                    player1.value = player1.value - pvalue1
                    player1.calc_hand()
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
                    player2.calc_hand()
                    pvalue2 = player2.value
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    stand = 1
                    while dealer.value < 17:
                        dealer.deal_card(deck.deal())
                        dealer.value = dealer.value - dvalue
                        dealer.calc_hand()
                        dvalue = dealer.value
                        
                    #Displays rest of dealer's hand and his score
                    show_score(650, 250, dealer.value)
                    screen.blit(card_images[dealer.cards[1]], (600, 10))
                    pygame.display.update(c_img_rect32)
                    
                    
                    if dealer.cardcount >= 3:
                        screen.blit(card_images[dealer.cards[2]], (730, 10))
                        pygame.display.update(c_img_rect33)
                        

                    if dealer.cardcount >= 4:
                        screen.blit(card_images[dealer.cards[3]], (860, 10))
                        pygame.display.update(c_img_rect34)
                        
                    
                    if dealer.cardcount >= 5:
                        screen.blit(card_images[dealer.cards[4]], (990, 10))
                        pygame.display.update(c_img_rect35)
                        
                    
                    #checks who wins
                    if dealer.value > 21:
                        result("HOUSE BUST")
                        winners("HOUSE BUST")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_2()
                    elif player1.value == dealer.value:
                        if player2.value == dealer.value:
                            result( "Player 1 and Player 2 Push")
                            winners("Player 1 and Player 2 Push")
                            pygame.display.update()
                            pygame.time.delay(4000)
                            run = False
                            scenario_2()
                        elif player2.value > dealer.value:
                            result("Player 1 Push and Player 2 Wins")
                            winners("Player 1 Push and Player 2 Wins")
                            pygame.display.update()
                            pygame.time.delay(4000)
                            run = False
                            scenario_2()
                        elif player2.value < dealer.value:
                            result( "Player 1 Push and Player 2 Loses")
                            winners("Player 1 Push and Player 2 Loses")
                            pygame.display.update()
                            pygame.time.delay(4000)
                            run = False
                            scenario_2()
                    elif player2.value == dealer.value:
                        if player1.value > dealer.value:
                            result( "Player 1 Wins and Player 2 Push")
                            winners("Player 1 Wins and Player 2 Push")
                            pygame.display.update()
                            pygame.time.delay(4000)
                            run = False
                            scenario_2()
                        elif player1.value < dealer.value:
                            result("Player 1 Loses and Player 2 Push")
                            winners("Player 1 Loses and Player 2 Push")
                            pygame.display.update()
                            pygame.time.delay(4000)
                            run = False
                            scenario_2()
                    elif player1.value > dealer.value:
                        if player2.value > dealer.value:
                            result("Player 1 and Player 2 Win")
                            winners("Player 1 and Player 2 Win")
                            pygame.display.update()
                            pygame.time.delay(4000)
                            run = False
                            scenario_2()
                        elif player2.value < dealer.value:
                            result("Player 1 Wins and Player 2 Loses")
                            winners("Player 1 Wins and Player 2 Loses")
                            pygame.display.update()
                            pygame.time.delay(4000)
                            run = False
                            scenario_2()
                    elif player2.value > dealer.value:
                        result("Player 1 Loses and Player 2 Wins")
                        winners("Player 1 Loses and Player 2 Wins")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_2()
                    else:
                        result("Player 1 and Player 2 Lose")
                        winners("Player 1 and Player 2 Lose")
                        pygame.display.update()
                        pygame.time.delay(4000)
                        run = False
                        scenario_2()
                        
            elif player1.value > 21 and player2.value > 21:
                result("Player 1 and Player 2 Bust")
                winners("Player 1 and Player 2 Bust")
                pygame.display.update()
                pygame.time.delay(4000)
                run = False
                scenario_2()
            elif player2.value >21:
                while dealer.value < 17:
                    dealer.deal_card(deck.deal())
                    dealer.value = dealer.value - dvalue
                    dealer.calc_hand()
                    dvalue = dealer.value
                    
                
                #Displays rest of dealer's hand and his score
                show_score(650, 250, dealer.value)
                screen.blit(card_images[dealer.cards[1]], (600, 10))
                pygame.display.update(c_img_rect32)
                
                
                if dealer.cardcount >= 3:
                    screen.blit(card_images[dealer.cards[2]], (730, 10))
                    pygame.display.update(c_img_rect33)
                    

                if dealer.cardcount >= 4:
                    screen.blit(card_images[dealer.cards[3]], (860, 10))
                    pygame.display.update(c_img_rect34)
                    
                
                if dealer.cardcount >= 5:
                    screen.blit(card_images[dealer.cards[4]], (990, 10))
                    pygame.display.update(c_img_rect35)
                    

                #Displays the result
                
                if dealer.value > 21:
                    result("Player 1 Wins and Player 2 Loses")
                    winners("Player 1 Wins and Player 2 Loses")
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    scenario_2()
                elif player1.value == dealer.value:
                    result("Player 1 Push and Player 2 Bust")
                    winners("Player 1 Push and Player 2 Bust")
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    scenario_2()
                elif player1.value > dealer.value:
                    result("Player 1 Wins and Player 2 Bust")
                    winners("Player 1 Wins and Player 2 Bust")
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    scenario_2()
                elif player2.value < dealer.value:
                    result("Player 1 Loses and Player 2 Bust")
                    winners("Player 1 Loses and Player 2 Bust")
                    pygame.display.update()
                    pygame.time.delay(4000)
                    run = False
                    scenario_2()
        fpsClock.tick(FPS)
        pygame.display.flip()
        


main_menu()
