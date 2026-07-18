import random

from art import logo, vs
from game_data import data


def check_answer(user_choice, a_followers, b_followers):
    if a_followers > b_followers and user_choice == "a":
        return True
    elif a_followers < b_followers and user_choice == "b":
        return True
    else:
        return False

print(logo)

choice_A = random.choice(data)
choice_B = random.choice(data)
score = 0
game_should_continue = True

while game_should_continue:
    choice_A = choice_B
    choice_B = random.choice(data)
    while choice_B == choice_A:
        choice_B = random.choice(data)

    print(f" Compare A: {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}")
    print(vs)
    print(f" Against B: {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}")

    user_choice = input("Who has more followers?: Type 'A' or 'B' ").lower()
    print("\n" * 20)
    print(logo)

    a_followers = choice_A["follower_count"]
    b_followers = choice_B["follower_count"]
    is_correct = check_answer(user_choice, a_followers, b_followers)

    if is_correct:
        score += 1
        print("You're right! Current score:", score)
    else:
        print("Sorry, that's wrong. final score:", score)
        game_should_continue = False




