import random
import itertools


card_deck_clubs = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "CT", "CJ", "CQ", "CK"]
card_deck_diamonds = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "DT", "DJ", "DQ", "DK"]
card_deck_hearts = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "HT", "HJ", "HQ", "HK"]
card_deck_spades = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "ST", "SJ", "SQ", "SK"]

playing_card_deck = card_deck_clubs + card_deck_diamonds + card_deck_hearts + card_deck_spades
#print(playing_card_deck)

shuffled_deck = random.sample(playing_card_deck, len(playing_card_deck))
print(shuffled_deck)

board = []

shuffled_deck.pop()
shuffled_deck.pop()

board.append(shuffled_deck.pop())
board.append(shuffled_deck.pop())
board.append(shuffled_deck.pop())
board.append(shuffled_deck.pop())
board.append(shuffled_deck.pop())

print(board)
#print(shuffled_deck)

bet_coin = 1
betting_money = 50 * bet_coin
casino_money = 0

print("Do you want to discard cards? Answer with Yes or No.")
x =input()
#print(x)


if x == "Yes":
    print("How many cards?")
    s = input()
    #print(type(s))
    sum = []
    for k in range(int(s)):
        print("Select the number of card to discard!")
        a = input()
        sum.append(int(a)-1)
    
    #print(sum)
    sum = sum[::-1]
    #print(sum)
    
    for i in sum:
        del board[i]
    print(board)

    shuffled_deck.pop()
    for i in range(len(sum)):
        board.append(shuffled_deck.pop())
    
    print(board)

new_board = []
for i in board:
    new_board.append(list(i))
print(new_board)    


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

print(club_counter,diamond_counter,heart_counter,spade_counter)


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


print(counter_1,counter_2,counter_3,counter_4,counter_5,counter_6,counter_7,counter_8,counter_9,counter_T,counter_J,counter_Q,counter_K)


if club_counter == 5 or diamond_counter == 5 or heart_counter == 5 or spade_counter == 5:
    if counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K == 1 and counter_1 == 1:
        betting_money = betting_money + 800 * bet_coin
        print("Royal Flush")
    elif counter_1 == 1 and counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    elif counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K ==1 :
        betting_money = betting_money + 50 * bet_coin
        print("Straight Flush")
    else:
        betting_money = betting_money + 6 * bet_coin
        print("Flush")
elif counter_1 == 4 or counter_2 == 4 or counter_3 == 4 or counter_4 == 4 or counter_5 == 4 or counter_6 == 4 or counter_7 == 4 or counter_8 == 4 or counter_9 == 4 or counter_T == 4 or counter_J == 4 or counter_Q == 4 or counter_K == 4:
    betting_money = betting_money + 25 * bet_coin
    print("Four of a Kind")
elif counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3:
    if counter_1 == 2 or counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 9 * bet_coin
        print("Full House")
    else:
        betting_money = betting_money + 3 * bet_coin
        print("Three of a Kind")
elif counter_1 == 1 and counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_2 == 1 and counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_3 == 1 and counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_4 == 1 and counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_5 == 1 and counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_6 == 1 and counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_7 == 1 and counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_8 == 1 and counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_9 == 1 and counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_T == 1 and counter_J == 1 and counter_Q == 1 and counter_K == 1 and counter_1 ==1 :
    betting_money = betting_money + 4 * bet_coin
    print("Straight")
elif counter_1 == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 1 * bet_coin
        print("One Pair")
elif counter_2 == 2:
    if counter_1 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_3 == 2:
    if counter_2 == 2 or counter_1 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_4 == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_1 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_5 == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_1 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_6 == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_1 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_7 == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_1 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_8 == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_1 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_9 == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_1 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_T == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_1 == 2 or counter_J == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 0 * bet_coin
        print("One Pair")
elif counter_J == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_1 == 2 or counter_Q == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 1 * bet_coin
        print("One Pair")
elif counter_Q == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_1 == 2 or counter_K == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 1 * bet_coin
        print("One Pair")
elif counter_K == 2:
    if counter_2 == 2 or counter_3 == 2 or counter_4 == 2 or counter_5 == 2 or counter_6 == 2 or counter_7 == 2 or counter_8 == 2 or counter_9 == 2 or counter_T == 2 or counter_J == 2 or counter_Q == 2 or counter_1 == 2:
        betting_money = betting_money + 2 * bet_coin
        print("Two Pair")
    elif not(counter_1 == 3 or counter_2 == 3 or counter_3 == 3 or counter_4 == 3 or counter_5 == 3 or counter_6 == 3 or counter_7 == 3 or counter_8 == 3 or counter_9 == 3 or counter_T == 3 or counter_J == 3 or counter_Q == 3 or counter_K == 3):
        betting_money = betting_money + 1 * bet_coin
        print("One Pair")
else:
    betting_money = betting_money + 0 * bet_coin
    print("No Pair")