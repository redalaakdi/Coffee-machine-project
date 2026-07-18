enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope (it exist within functions)
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global Scope (it is outside the function)
player_health = 10
def game():
    def drink_potion():
        potion_strength = 5
        print(potion_strength)
        print(player_health)
    drink_potion()
print(player_health)



def my_function():
    my_local_var = 9
    print(my_local_var)

my_function()

def make_sandwich():
    filling = "tuna"   # local to this function
    print(filling)


x = "global"
def outer():
    x = "local"
    print(x)
outer()
print(x)

attempts = 5
def reset_attempts():
    attempts = 10
reset_attempts()
print(attempts)

MAX_GUESSES = 10
GAME_TITLE = "Number Guessing Game"

def update_score():
    global total_score
    total_score += 1
    print(total_score)

total_score = 0
update_score()



