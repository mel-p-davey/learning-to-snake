import copy
import random
import os
val_of_comp_hand = None
val_of_player_hand = None
working_deck = None


card_deck ={"A": [11,11,11,11], "2":[2,2,2,2], "3":[3,3,3,3], "4":[4,4,4,4],
 "5":[5,5,5,5], "6":[6,6,6,6], "7":[7,7,7,7], "8":[8,8,8,8], "9":[9,9,9,9], "10":[10,10,10,10],
 "J":[10,10,10,10], "Q":[10,10,10,10], "K":[10,10,10,10]}


def initialize_game():
    os.system('cls')
    print("New game!")
    global working_deck
    working_deck = copy.deepcopy(card_deck)
        
def players_first_hand_pick():
    print("First up, the player\n")
    first_card_num=2
    players_hand = [random.choice(list(working_deck)) for i in range(first_card_num)]
    print(players_hand)
    return players_hand

def val_players_first_hand(players_hand):
    global val_of_player_hand
    global working_deck
    val_of_player_hand = 0
    for i in players_hand:
        val_of_player_hand+= working_deck[i][0]
        working_deck[i]=working_deck[i][1:]
    if "A" in players_hand:
        if val_of_player_hand > 21:
            val_of_player_hand-=10
    print(f"The value of your chosen card(s) is {val_of_player_hand}")
    return val_of_player_hand 

def computers_first_hand_pick():
    print("Now, the computer\n")
    global working_deck
    first_card_num=2
    comp_hand = [random.choice(list(working_deck)) for i in range(first_card_num)]
    return comp_hand

def val_comp_first_hand(comp_hand):
    global val_of_comp_hand
    global working_deck
    val_of_comp_hand = 0
    for i in comp_hand:
        val_of_comp_hand+= working_deck[i][0]
        working_deck[i]=working_deck[i][1:]
    print("The computer has gone. ")
    return val_of_comp_hand 

def pick_card():
    a = int(input("How many cards would you like to pick?:  "))
    global working_deck
    additional_hand_picked = [random.choice(list(working_deck)) for i in range(a)]
    print(additional_hand_picked)
    return additional_hand_picked

def pick_comp_card():
    global working_deck
    additional_comp_hand_picked = [random.choice(list(working_deck))]
    return additional_comp_hand_picked

def value_of_deck(a):
    global working_deck
    additional_value = 0
    for i in a:
        additional_value+= working_deck[i][0]
        working_deck[i]=working_deck[i][1:]
    return additional_value

def is_there_ace(a):
    if "A" in a:
        return True     

def players_additional_card():
    answer = input("Would you like to pick another card Player? Type Y for Yes and N for No  ")
    if answer == "N":
        return False

def computers_additional_card():
    global val_of_comp_hand
    print("Let us see if the computer will pick another card...\n")
    if (21 - val_of_comp_hand) < 3:
        print("Computer will pass on this turn\n ")
        return False
    elif (21 - val_of_comp_hand) <6:
        print("Computer will pick a card on this turn. \n Done.")
        chance30 = [True, True, True, False, False, False, False, False, False, False]
        should_pick = random.choice(list(chance30))
        if should_pick == True:
            return True
        return
    elif (21 - val_of_comp_hand) <8:
        print("Computer will pick a card on this turn. \n Done.")
        chance70 = [True, True, True, True, True, True, True, False, False, False]
        should_pick = random.choice(list(chance70))
        if should_pick == True:
            return True
        return
    elif (21 - val_of_comp_hand) <11:
        print("Computer will pick a card on this turn. \n Done.")
        return True
    else:
        print("Computer will pick a card on this turn. \n Done.")
        return True

def compare_hands():
    global val_of_player_hand
    global val_of_comp_hand
    if val_of_player_hand == val_of_comp_hand:
        print(f"We have a draw! The computer\'s hand is {val_of_comp_hand}")
    elif val_of_player_hand> 21 and val_of_comp_hand >21:
        print(f"You both lose, the computer\'s hand is {val_of_comp_hand}")
    elif val_of_player_hand> 21:
        print(f"The player loses! The value of computer\'s hand is {val_of_comp_hand}")
    elif val_of_comp_hand >21:
        print(f"The computer loses. The value of computer\'s hand is {val_of_comp_hand}")
    elif val_of_player_hand > val_of_comp_hand:
        print(f"The player wins, the value of computer\'s hand is {val_of_comp_hand}")
    else:
        print(f"The computer wins, the value of computer\'s hand is {val_of_comp_hand}")

def continue_game_player():
    if players_additional_card() != False:
        return True

def continue_game_comp():
    if computers_additional_card() != False:
        return True

def prompt_to_playagain():
    play_again_answer = input("Would you like to play a game of Blackjack? Type Y for Yes and N for No. ")
    if play_again_answer == "Y":
        return True
    else:
        print("Goodbye")
        return False

def game():
    global val_of_comp_hand
    global val_of_player_hand
    initialize_game()
    val_players_first_hand(players_first_hand_pick())
    val_comp_first_hand(computers_first_hand_pick())

    while continue_game_player() ==True:
            deck_pick_player = pick_card()
            val_next_hand = value_of_deck(deck_pick_player)
            val_of_player_hand = val_next_hand + val_of_player_hand
            if is_there_ace(deck_pick_player) == True:
                if val_of_player_hand > 21:
                    val_of_player_hand-=10
            print(f"The players hand is now equal to {val_of_player_hand}")
    while continue_game_comp() == True:
            deck_pick_comp = pick_comp_card()
            val_next_comp_hand = value_of_deck(deck_pick_comp)
            val_of_comp_hand = val_next_comp_hand + val_of_comp_hand
            if is_there_ace(deck_pick_comp) == True:
                if val_of_comp_hand > 21:
                    val_of_comp_hand-=10
    compare_hands()
    if prompt_to_playagain() != False:
        game()

game()
