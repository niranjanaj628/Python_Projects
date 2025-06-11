#BlackJack game : Day-11
import random

  
def deal_card():
    '''Returns random card from the deck'''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    '''Returns the sum of the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score > 21:
        return "Opponent went over, you win"
    elif user_score > computer_score: 
        return "You win"
    else:
        return "You lose"
    
def play_game():
    player_cards = []
    comp_cards = []
    game_over = False

    player_score = -1
    comp_score = -1

    for _ in range(2):
            player_cards.append(deal_card())
            comp_cards.append(deal_card())
            
    while not game_over:
            
        player_score = calculate_score(player_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print (f"Computer's first card: {comp_cards[0]}")

        if player_score == 0 or comp_score == 0 or player_score > 21 or comp_score >21:
            game_over = True
        else:
            new_card = input("Type 'y' to get another card, type 'n' to pass: " )
            if new_card == 'y':
                player_cards.append(deal_card())
                
            else:
                game_over = True
    
    comp_score = calculate_score(comp_cards)
             
    while comp_score != 0 and comp_score <17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")

    print(compare(player_score, comp_score))

while input("Do you wanna play another game? Type 'y' or 'n': ") == 'y':
    play_game()