
def calculate():
    result = 5 * 10
    return result
answer = calculate()
print(answer)

player_name = 100

def greet():
    print(player_name)

def farewell():
    print(player_name * 2 )

greet()
farewell()

score = 3
def add_point():
    global score
    score -= 1
    print(score)

add_point()

MAX_GUESSES = 10
MIN_NUMBER = 1
MAX_NUMBER = 100

def start_game():
    print(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}")
    print(f"You have {MAX_GUESSES} attempts")



