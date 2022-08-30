from typing import TextIO
import pygame
import sys
import os
import random


pygame.init()

WIDTH, HEIGHT = 650, 500
WINDOW =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jacks Or Better Poker!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

FPS = 60

SMALLFONT1 = pygame.font.SysFont('Times New Roman',90)
SMALLFONT2 = pygame.font.SysFont('Times New Roman',40)
SMALLFONT3 = pygame.font.SysFont('Times New Roman',30)
SMALLFONT4 = pygame.font.SysFont('Times New Roman',80)

TEXT1 = SMALLFONT1.render("Jack's or Better",True, (255, 0, 0))
TEXT2 = SMALLFONT1.render("Poker Game",True, (255, 0, 0))
TEXT3 = SMALLFONT2.render("PLAY",True, (255, 0, 0))
TEXT4 = SMALLFONT2.render("QUIT",True, (255, 0, 0))
TEXT5 = SMALLFONT3.render('Hold',True, (255, 0, 0))
TEXT6 = SMALLFONT3.render('Held',True, (255, 0, 0))
TEXT7 = SMALLFONT3.render('Continue',True, (255, 0, 0))
TEXT8 = SMALLFONT3.render('Playing',True, (255, 0, 0))
TEXT9 = SMALLFONT3.render('Quit to',True, (255, 0, 0))
TEXT10 = SMALLFONT3.render('Main Menu',True, (255, 0, 0))

RESIZE_WIDTH, RESIZE_HEIGHT = 100, 150

#asset loading and resizing
#download needed from https://code.google.com/archive/p/vector-playing-cards/ for the cards to show up
C1_image = pygame.image.load(os.path.join('PNG-cards-1.3','ace_of_clubs.png'))
C1 = pygame.transform.scale(C1_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D1_image = pygame.image.load(os.path.join('PNG-cards-1.3','ace_of_diamonds.png'))
D1 = pygame.transform.scale(D1_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H1_image = pygame.image.load(os.path.join('PNG-cards-1.3','ace_of_hearts.png'))
H1 = pygame.transform.scale(H1_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S1_image = pygame.image.load(os.path.join('PNG-cards-1.3','ace_of_spades.png'))
S1 = pygame.transform.scale(S1_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C2_image = pygame.image.load(os.path.join('PNG-cards-1.3','2_of_clubs.png'))
C2 = pygame.transform.scale(C2_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D2_image = pygame.image.load(os.path.join('PNG-cards-1.3','2_of_diamonds.png'))
D2 = pygame.transform.scale(D2_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H2_image = pygame.image.load(os.path.join('PNG-cards-1.3','2_of_hearts.png'))
H2 = pygame.transform.scale(H2_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S2_image = pygame.image.load(os.path.join('PNG-cards-1.3','2_of_spades.png'))
S2 = pygame.transform.scale(S2_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C3_image = pygame.image.load(os.path.join('PNG-cards-1.3','3_of_clubs.png'))
C3 = pygame.transform.scale(C3_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D3_image = pygame.image.load(os.path.join('PNG-cards-1.3','3_of_diamonds.png'))
D3 = pygame.transform.scale(D3_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H3_image = pygame.image.load(os.path.join('PNG-cards-1.3','3_of_hearts.png'))
H3 = pygame.transform.scale(H3_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S3_image = pygame.image.load(os.path.join('PNG-cards-1.3','3_of_spades.png'))
S3 = pygame.transform.scale(S3_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C4_image = pygame.image.load(os.path.join('PNG-cards-1.3','4_of_clubs.png'))
C4 = pygame.transform.scale(C4_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D4_image = pygame.image.load(os.path.join('PNG-cards-1.3','4_of_diamonds.png'))
D4 = pygame.transform.scale(D4_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H4_image = pygame.image.load(os.path.join('PNG-cards-1.3','4_of_hearts.png'))
H4 = pygame.transform.scale(H4_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S4_image = pygame.image.load(os.path.join('PNG-cards-1.3','4_of_spades.png'))
S4 = pygame.transform.scale(S4_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C5_image = pygame.image.load(os.path.join('PNG-cards-1.3','5_of_clubs.png'))
C5 = pygame.transform.scale(C5_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D5_image = pygame.image.load(os.path.join('PNG-cards-1.3','5_of_diamonds.png'))
D5 = pygame.transform.scale(D5_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H5_image = pygame.image.load(os.path.join('PNG-cards-1.3','5_of_hearts.png'))
H5 = pygame.transform.scale(H5_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S5_image = pygame.image.load(os.path.join('PNG-cards-1.3','5_of_spades.png'))
S5 = pygame.transform.scale(S5_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C6_image = pygame.image.load(os.path.join('PNG-cards-1.3','6_of_clubs.png'))
C6 = pygame.transform.scale(C6_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D6_image = pygame.image.load(os.path.join('PNG-cards-1.3','6_of_diamonds.png'))
D6 = pygame.transform.scale(D6_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H6_image = pygame.image.load(os.path.join('PNG-cards-1.3','6_of_hearts.png'))
H6 = pygame.transform.scale(H6_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S6_image = pygame.image.load(os.path.join('PNG-cards-1.3','6_of_spades.png'))
S6 = pygame.transform.scale(S6_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C7_image = pygame.image.load(os.path.join('PNG-cards-1.3','7_of_clubs.png'))
C7 = pygame.transform.scale(C7_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D7_image = pygame.image.load(os.path.join('PNG-cards-1.3','7_of_diamonds.png'))
D7 = pygame.transform.scale(D7_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H7_image = pygame.image.load(os.path.join('PNG-cards-1.3','7_of_hearts.png'))
H7 = pygame.transform.scale(H7_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S7_image = pygame.image.load(os.path.join('PNG-cards-1.3','7_of_spades.png'))
S7 = pygame.transform.scale(S7_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C8_image = pygame.image.load(os.path.join('PNG-cards-1.3','8_of_clubs.png'))
C8 = pygame.transform.scale(C8_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D8_image = pygame.image.load(os.path.join('PNG-cards-1.3','8_of_diamonds.png'))
D8 = pygame.transform.scale(D8_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H8_image = pygame.image.load(os.path.join('PNG-cards-1.3','8_of_hearts.png'))
H8 = pygame.transform.scale(H8_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S8_image = pygame.image.load(os.path.join('PNG-cards-1.3','8_of_spades.png'))
S8 = pygame.transform.scale(S8_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
C9_image = pygame.image.load(os.path.join('PNG-cards-1.3','9_of_clubs.png'))
C9 = pygame.transform.scale(C9_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
D9_image = pygame.image.load(os.path.join('PNG-cards-1.3','9_of_diamonds.png'))
D9 = pygame.transform.scale(D9_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
H9_image = pygame.image.load(os.path.join('PNG-cards-1.3','9_of_hearts.png'))
H9 = pygame.transform.scale(H9_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
S9_image = pygame.image.load(os.path.join('PNG-cards-1.3','9_of_spades.png'))
S9 = pygame.transform.scale(S9_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
CT_image = pygame.image.load(os.path.join('PNG-cards-1.3','10_of_clubs.png'))
CT = pygame.transform.scale(CT_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
DT_image = pygame.image.load(os.path.join('PNG-cards-1.3','10_of_diamonds.png'))
DT = pygame.transform.scale(DT_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
HT_image = pygame.image.load(os.path.join('PNG-cards-1.3','10_of_hearts.png'))
HT = pygame.transform.scale(HT_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
ST_image = pygame.image.load(os.path.join('PNG-cards-1.3','10_of_spades.png'))
ST = pygame.transform.scale(ST_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
CJ_image = pygame.image.load(os.path.join('PNG-cards-1.3','jack_of_clubs2.png'))
CJ = pygame.transform.scale(CJ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
DJ_image = pygame.image.load(os.path.join('PNG-cards-1.3','jack_of_diamonds2.png'))
DJ = pygame.transform.scale(DJ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
HJ_image = pygame.image.load(os.path.join('PNG-cards-1.3','jack_of_hearts2.png'))
HJ = pygame.transform.scale(HJ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
SJ_image = pygame.image.load(os.path.join('PNG-cards-1.3','jack_of_spades2.png'))
SJ = pygame.transform.scale(SJ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
CQ_image = pygame.image.load(os.path.join('PNG-cards-1.3','queen_of_clubs2.png'))
CQ = pygame.transform.scale(CQ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
DQ_image = pygame.image.load(os.path.join('PNG-cards-1.3','queen_of_diamonds2.png'))
DQ = pygame.transform.scale(DQ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
HQ_image = pygame.image.load(os.path.join('PNG-cards-1.3','queen_of_hearts2.png'))
HQ = pygame.transform.scale(HQ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
SQ_image = pygame.image.load(os.path.join('PNG-cards-1.3','queen_of_spades2.png'))
SQ = pygame.transform.scale(SQ_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
CK_image = pygame.image.load(os.path.join('PNG-cards-1.3','king_of_clubs2.png'))
CK = pygame.transform.scale(CK_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
DK_image = pygame.image.load(os.path.join('PNG-cards-1.3','king_of_diamonds2.png'))
DK = pygame.transform.scale(DK_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
HK_image = pygame.image.load(os.path.join('PNG-cards-1.3','king_of_hearts2.png'))
HK = pygame.transform.scale(HK_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
SK_image = pygame.image.load(os.path.join('PNG-cards-1.3','king_of_spades2.png'))
SK = pygame.transform.scale(SK_image, (RESIZE_WIDTH, RESIZE_HEIGHT))
JOKER_image = pygame.image.load(os.path.join('PNG-cards-1.3','red_joker.png'))
JOKER = pygame.transform.scale(JOKER_image, (RESIZE_WIDTH, RESIZE_HEIGHT))


CARD_DECK_CLUBS = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "CT", "CJ", "CQ", "CK"]
CARD_DECK_DIAMONDS = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "DT", "DJ", "DQ", "DK"]
CARD_DECK_HEARTS = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "HT", "HJ", "HQ", "HK"]
CARD_DECK_SPADES = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "ST", "SJ", "SQ", "SK"]
PLAYING_CARD_DECK = CARD_DECK_CLUBS + CARD_DECK_DIAMONDS + CARD_DECK_HEARTS + CARD_DECK_SPADES


OUTPUT = [JOKER, JOKER, JOKER, JOKER, JOKER]

def card_checker(board):
    for i in range(len(board)):
        if board[i] == "C1":
            OUTPUT[i] = C1
        elif board[i] == "C2":
            OUTPUT[i] = C2
        elif board[i] == "C3":
            OUTPUT[i] = C3
        elif board[i] == "C4":
            OUTPUT[i] = C4
        elif board[i] == "C5":
            OUTPUT[i] = C5
        elif board[i] == "C6":
            OUTPUT[i] = C6
        elif board[i] == "C7":
            OUTPUT[i] = C7
        elif board[i] == "C8":
            OUTPUT[i] = C8
        elif board[i] == "C9":
            OUTPUT[i] = C9
        elif board[i] == "CT":
            OUTPUT[i] = CT
        elif board[i] == "CJ":
            OUTPUT[i] = CJ
        elif board[i] == "CQ":
            OUTPUT[i] = CQ
        elif board[i] == "CK":
            OUTPUT[i] = CK
        elif board[i] == "D1":
            OUTPUT[i] = D1
        elif board[i] == "D2":
            OUTPUT[i] = D2
        elif board[i] == "D3":
            OUTPUT[i] = D3
        elif board[i] == "D4":
            OUTPUT[i] = D4
        elif board[i] == "D5":
            OUTPUT[i] = D5
        elif board[i] == "D6":
            OUTPUT[i] = D6
        elif board[i] == "D7":
            OUTPUT[i] = D7
        elif board[i] == "D8":
            OUTPUT[i] = D8
        elif board[i] == "D9":
            OUTPUT[i] = D9
        elif board[i] == "DT":
            OUTPUT[i] = DT
        elif board[i] == "DJ":
            OUTPUT[i] = DJ
        elif board[i] == "DQ":
            OUTPUT[i] = DQ
        elif board[i] == "DK":
            OUTPUT[i] = DK
        elif board[i] == "H1":
            OUTPUT[i] = H1
        elif board[i] == "H2":
            OUTPUT[i] = H2
        elif board[i] == "H3":
            OUTPUT[i] = H3
        elif board[i] == "H4":
            OUTPUT[i] = H4
        elif board[i] == "H5":
            OUTPUT[i] = H5
        elif board[i] == "H6":
            OUTPUT[i] = H6
        elif board[i] == "H7":
            OUTPUT[i] = H7
        elif board[i] == "H8":
            OUTPUT[i] = H8
        elif board[i] == "H9":
            OUTPUT[i] = H9
        elif board[i] == "HT":
            OUTPUT[i] = HT
        elif board[i] == "HJ":
            OUTPUT[i] = HJ
        elif board[i] == "HQ":
            OUTPUT[i] = HQ
        elif board[i] == "HK":
            OUTPUT[i] = HK
        elif board[i] == "S1":
            OUTPUT[i] = S1
        elif board[i] == "S2":
            OUTPUT[i] = S2
        elif board[i] == "S3":
            OUTPUT[i] = S3
        elif board[i] == "S4":
            OUTPUT[i] = S4
        elif board[i] == "S5":
            OUTPUT[i] = S5
        elif board[i] == "S6":
            OUTPUT[i] = S6
        elif board[i] == "S7":
            OUTPUT[i] = S7
        elif board[i] == "S8":
            OUTPUT[i] = S8
        elif board[i] == "S9":
            OUTPUT[i] = S9
        elif board[i] == "ST":
            OUTPUT[i] = ST
        elif board[i] == "SJ":
            OUTPUT[i] = SJ
        elif board[i] == "SQ":
            OUTPUT[i] = SQ
        elif board[i] == "SK":
            OUTPUT[i] = SK

def board_phase1(shuffled_deck):
    board = []
    shuffled_deck.pop()
    shuffled_deck.pop()

    board.append(shuffled_deck.pop())
    board.append(shuffled_deck.pop())
    board.append(shuffled_deck.pop())
    board.append(shuffled_deck.pop())
    board.append(shuffled_deck.pop())
    
    card_checker(board)

    return board


bet_coin = 1
betting_money = 20 * bet_coin

def board_phase2(cc1, cc2, cc3, cc4, cc5, board, shuffled_deck):
    global betting_money
    shuffled_deck.pop()
    if cc1 % 2 == 0:
        board[0] = shuffled_deck.pop()
    if cc2 % 2 == 0:
        board[1] = shuffled_deck.pop()
    if cc3 % 2 == 0:
        board[2] = shuffled_deck.pop()
    if cc4 % 2 == 0:
        board[3] = shuffled_deck.pop()
    if cc5 % 2 == 0:
        board[4] = shuffled_deck.pop()

    
    card_checker(board)
    new_board = []
    for i in board:
        new_board.append(list(i))
    

    club_counter = 0
    diamond_counter = 0
    heart_counter = 0
    spade_counter = 0
    for i in new_board:
        if i[0] == "C":
            club_counter = club_counter + 1
        elif i[0] == "D":
            diamond_counter = diamond_counter + 1
        elif i[0] == "H":
            heart_counter = heart_counter + 1
        elif i[0] == "S":
            spade_counter = spade_counter + 1
    
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    counter_5 = 0
    counter_6 = 0
    counter_7 = 0
    counter_8 = 0
    counter_9 = 0
    counter_T = 0
    counter_J = 0
    counter_Q = 0
    counter_K = 0
    for i in new_board:
        if i[1] == "1":
            counter_1 = counter_1 + 1
        elif i[1] == "2":
            counter_2 = counter_2 + 1
        elif i[1] == "3":
            counter_3 = counter_3 + 1
        elif i[1] == "4":
            counter_4 = counter_4 + 1
        elif i[1] == "5":
            counter_5 = counter_5 + 1
        elif i[1] == "6":
            counter_6 = counter_6 + 1
        elif i[1] == "7":
            counter_7 = counter_7 + 1            
        elif i[1] == "8":
            counter_8 = counter_8 + 1
        elif i[1] == "9":
            counter_9 = counter_9 + 1
        elif i[1] == "T":
            counter_T = counter_T + 1
        elif i[1] == "J":
            counter_J = counter_J + 1
        elif i[1] == "Q":
            counter_Q = counter_Q + 1
        elif i[1] == "K":
            counter_K = counter_K + 1
    
    if club_counter == 5 or diamond_counter == 5 or heart_counter == 5 or spade_counter == 5:
        if counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K == 1 and counter_1 == 1:
            betting_money = betting_money + 800 * bet_coin
            return "Royal Flush"
        elif counter_1 == 1 and counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        elif counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K ==1 :
            betting_money = betting_money + 50 * bet_coin
            return "Straight Flush"
        else:
            betting_money = betting_money + 6 * bet_coin
            return "Flush"
    elif counter_1 == 4 or counter_2 == 4 or counter_3 == 4 or counter_4 == 4 or counter_5 == 4 or counter_6 == 4 or counter_7 == 4 or counter_8 == 4 or counter_9 == 4 or counter_T == 4 or counter_J == 4 or counter_Q == 4 or counter_K == 4:
        betting_money = betting_money + 25 * bet_coin
        return "Four of a Kind"
    elif counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3:
        if counter_1 == 2 or counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 9 * bet_coin
            return "Full House"
        else:
            betting_money = betting_money + 3 * bet_coin
            return "Three of a Kind"
    elif counter_1 == 1 and counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K == 1 and counter_1 ==1 :
        betting_money = betting_money + 4 * bet_coin
        return "Straight"
    elif counter_1 == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 1 * bet_coin
            return "Pair of Aces"
    elif counter_2 == 2:
        if counter_1 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_3 == 2:
        if counter_2 == 2 or counter_1 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_4 == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_1 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_5 == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_1 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_6 == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_1 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_7 == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_1 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_8 == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_1 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_9 == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_1 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_T == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_1 == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 0 * bet_coin
            return "One Pair"
    elif counter_J == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_1 == 2 or counter_Q == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 1 * bet_coin
            return "Pair of Jacks"
    elif counter_Q == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_1 == 2 or counter_K == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 1 * bet_coin
            return "Pair of Queens"
    elif counter_K == 2:
        if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_1 == 2:
            betting_money = betting_money + 2 * bet_coin
            return "Two Pair"
        elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
            betting_money = betting_money + 1 * bet_coin
            return "Pair of Kings"
    else:
        betting_money = betting_money + 0 * bet_coin
        return "No Pair"

def draw_intro():
    WINDOW.fill(WHITE)
    WINDOW.blit(TEXT1, (50, 50))
    WINDOW.blit(TEXT2, (100, 130))
    pygame.draw.rect(WINDOW, BLACK, [120, 350, 120, 50])
    WINDOW.blit(TEXT3, (132, 353))
    pygame.draw.rect(WINDOW, BLACK, [400, 350, 120, 50])
    WINDOW.blit(TEXT4, (412, 353))

    pygame.display.update()


#TEXT11 = SMALLFONT3.render(str(betting_money),True, (255, 0, 0))

def draw_window_p1(cc1, cc2, cc3, cc4, cc5):
    WINDOW.fill(WHITE)
    WINDOW.blit(OUTPUT[0], (50,100))
    WINDOW.blit(OUTPUT[1], (160,100))
    WINDOW.blit(OUTPUT[2], (270,100))
    WINDOW.blit(OUTPUT[3], (380,100))
    WINDOW.blit(OUTPUT[4], (490,100))
    if cc1 % 2 == 0:
        pygame.draw.rect(WINDOW, BLACK, [50, 300, 100, 30])
        WINDOW.blit(TEXT5, (72, 298 ))
    else:
        pygame.draw.rect(WINDOW, BLUE, [50, 300, 100, 30])
        WINDOW.blit(TEXT6, (72, 298 ))
        pygame.draw.rect(WINDOW, BLACK, [95, 275, 10, 10] )
    if cc2 % 2 == 0:
        pygame.draw.rect(WINDOW, BLACK, [160, 300, 100, 30])
        WINDOW.blit(TEXT5, (182, 298 ))
    else:
        pygame.draw.rect(WINDOW, BLUE, [160, 300, 100, 30])
        WINDOW.blit(TEXT6, (182, 298 ))
        pygame.draw.rect(WINDOW, BLACK, [205, 275, 10, 10] )
    if cc3 % 2 == 0:
        pygame.draw.rect(WINDOW, BLACK, [270, 300, 100, 30])
        WINDOW.blit(TEXT5, (292, 298 ))
    else:
        pygame.draw.rect(WINDOW, BLUE, [270, 300, 100, 30])
        WINDOW.blit(TEXT6, (292, 298 ))
        pygame.draw.rect(WINDOW, BLACK, [315, 275, 10, 10] )
    if cc4 % 2 == 0:
        pygame.draw.rect(WINDOW, BLACK, [380, 300, 100, 30])
        WINDOW.blit(TEXT5, (402, 298 ))
    else:
        pygame.draw.rect(WINDOW, BLUE, [380, 300, 100, 30])
        WINDOW.blit(TEXT6, (402, 298 ))
        pygame.draw.rect(WINDOW, BLACK, [425, 275, 10, 10] )
    if cc5 % 2 == 0:
        pygame.draw.rect(WINDOW, BLACK, [490, 300, 100, 30])
        WINDOW.blit(TEXT5, (512, 298 ))
    else:
        pygame.draw.rect(WINDOW, BLUE, [490, 300, 100, 30])
        WINDOW.blit(TEXT6, (512, 298 ))
        pygame.draw.rect(WINDOW, BLACK, [535, 275, 10, 10] )
    pygame.draw.rect(WINDOW, BLACK, [270, 400, 100, 30])
    global betting_money
    TEXT11 = SMALLFONT3.render(str(betting_money),True, (255, 0, 0))
    WINDOW.blit(TEXT11, (350, 50))
    pygame.display.update()

def draw_window_p2(xyz):
    WINDOW.fill(BLUE)
    WINDOW.blit(OUTPUT[0], (50,100))
    WINDOW.blit(OUTPUT[1], (160,100))
    WINDOW.blit(OUTPUT[2], (270,100))
    WINDOW.blit(OUTPUT[3], (380,100))
    WINDOW.blit(OUTPUT[4], (490,100))
    TEXT3 = SMALLFONT4.render(xyz, True, BLACK)
    WINDOW.blit(TEXT3, (180, 300))
    pygame.draw.rect(WINDOW, BLACK, [150, 400, 150, 60])
    WINDOW.blit(TEXT7, (170, 398))
    WINDOW.blit(TEXT8, (180, 428))
    pygame.draw.rect(WINDOW, BLACK, [350, 400, 150, 60])
    WINDOW.blit(TEXT9, (381, 396))
    WINDOW.blit(TEXT10, (355, 426))
    global betting_money
    TEXT11 = SMALLFONT3.render(str(betting_money),True, (255, 0, 0))
    WINDOW.blit(TEXT11, (350, 50))
    pygame.display.update()


cc_cont = False

def main():
    global cc_cont
    global betting_money
    clock = pygame.time.Clock()
    run = True
    ccquit = False
    if cc_cont == False:
        while run:
            clock.tick(FPS)
            MOUSE = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    ccquit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 120 <= MOUSE[0] <= 240 and 350 <= MOUSE[1] <= 400:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 400 <= MOUSE[0] <= 520 and 350 <= MOUSE[1] <= 400:
                        run = False
                        ccquit = True
        
            draw_intro()

    if run == False and ccquit == True:
        sys.exit()

    run = True
    cc1 = 0
    cc2 = 0
    cc3 = 0
    cc4 = 0
    cc5 = 0
    cc6 = False
    shuffled_deck = random.sample(PLAYING_CARD_DECK, len(PLAYING_CARD_DECK))
    board = board_phase1(shuffled_deck)
    betting_money -= 1

    while run:
        clock.tick(FPS)
        MOUSE = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= MOUSE[0] <= 150 and 300 <= MOUSE[1] <= 330:
                    cc1 +=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 160 <= MOUSE[0] <= 260 and 300 <= MOUSE[1] <= 330:
                    cc2 +=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 270 <= MOUSE[0] <= 370 and 300 <= MOUSE[1] <= 330:
                    cc3 +=1        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 380 <= MOUSE[0] <= 480 and 300 <= MOUSE[1] <= 330:
                    cc4 +=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 490 <= MOUSE[0] <= 590 and 300 <= MOUSE[1] <= 330:
                    cc5 +=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 270 <= MOUSE[0] <= 370 and 400 <= MOUSE[1] <= 430:
                    cc6 = True
                    run = False
        draw_window_p1(cc1, cc2, cc3, cc4, cc5)

    if run == False and cc6 == False:
        pygame.quit()
        sys.exit()

    run = True
    xyz = board_phase2(cc1, cc2, cc3, cc4, cc5, board, shuffled_deck)
    while run:
        clock.tick(FPS)
        MOUSE = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= MOUSE[0] <= 300 and 400 <= MOUSE[1] <= 460:
                    run = False
                    ccplay = True
                    cc_cont = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= MOUSE[0] <= 500 and 400 <= MOUSE[1] <= 460:
                    run = False
                    ccquit = True
                    cc_cont = False
                    betting_money = 20 * bet_coin
        
        draw_window_p2(xyz)

    print(betting_money)    
    main()



if __name__ == "__main__":
    main()
