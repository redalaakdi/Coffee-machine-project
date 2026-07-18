import random
LOGO = r'''  

________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/      
         '''
print(LOGO)
print("Welcome to the Number Guessing Game!")
def game_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5

def guess_the_number():
    global attempts
    while attempts > 0:
        print(f"You have {attempts} attempts remaining")
        guess = int(input("Make a Guess"))
        if guess > secret_number:
            print("too high")
            attempts -= 1
        elif guess < secret_number:
            print("too low")
            attempts -= 1
        elif guess == secret_number:
            print("You got it!")
            break
    if attempts == 0:
        print(f"You've run out of guesses. The answer was {secret_number}.")
play_again = "yes"
while play_again == "yes":
    print("I am thinking of a number between 1 and 100.")
    secret_number = random.randint(1,100)
    attempts = game_level()
    guess_the_number()
    play_again = input("Do you want to play again? (yes/no): ")

