import random
from art import logo
print(logo)
#game cards

def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def deal_cards():  #return one random card
        result = random.choice(cards)
        return result
    #hold 2 cards
    user_cards = []
    computer_cards = []
    user_cards.append(deal_cards())
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    computer_cards.append(deal_cards())

    def calculate_score(cards): # it takes the cards > verify > gives the result
        score = sum(cards)         # score
        if len(cards) == 2 and score == 21:    #Blackjack(21) > return 0
            return 0
        if score > 21 and 11 in cards:    #Ace(11) > 11 became 1
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
        return score
    calculate_score(user_cards)
    calculate_score(computer_cards)
    #Show user's cards + score & computer's first card
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    Condition = True  #Keep looping while user wants more cards
    while Condition:
        # y = one more card | n stops game
        user_turn = input("Type 'y' to get another card, type 'n' to pass:")
        if user_turn == "y":
            user_cards.append(deal_cards())
            print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
            if calculate_score(user_cards) > 21: #if score > 21 >> user lost the game
                print("You lost!")
                Condition = False
        elif user_turn == "n":
            Condition = False

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_cards())

    #Show final results
    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

    def compare(user_score, computer_score):
        if user_score == computer_score:
            print("Draw")
        elif user_score == 0:
            print("You win!")
        elif computer_score == 0:
            print("Computer wins!")
        elif user_score > 21:
            print("You lose!")
        elif computer_score > 21:
            print("Computer lose!")
        else:
            if user_score > computer_score:
                print("You win!")
            elif user_score < computer_score:
                print("Computer wins!")
    compare(user_score = calculate_score(user_cards), computer_score = calculate_score(computer_cards))

play_again = "y"
while play_again == "y":
    play_game()
    play_again = input("Would you like to play again? Type 'y' or 'n': ")

