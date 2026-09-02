import random
import replit

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    
    return card

def calculte_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has blackjack"
    elif u_score == 0:
        return "Win with a blackjack"
    elif u_score > 21:
        return "You went over you loss"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You loss"

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        

    while not is_game_over:
        user_score = calculte_score(user_cards)
        computer_score = calculte_score(computer_cards)

        print(f"Your cards: {user_cards} and your current score: {user_score}")
        print(f"computer frist card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score == 21:
            is_game_over = True

        else:
            user_should_deal = input("Type 'y' to get anther card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while user_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score =  calculte_score(computer_cards)
        
        
    print(f"Your final score {user_cards} and your final score: {user_score}")
    print(f"computer final score {computer_cards} and computer final score: {computer_score}")

    print(compare(user_score, computer_score))

    replit.clear()

while input("Do you want to play blackjack game: y or n: ") == "y":
    play_game()