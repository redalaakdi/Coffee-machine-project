# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

def greet_with (name, location):
    print(f"Hello {name}")
    print(f"what it is like in {location}?")
greet_with(location="London", name="Jack")




def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    score = int(str(first_digit) + str(second_digit))
    print(score)
calculate_love_score("Mohammed Reda", "Zainab Razak")




def calculate_love_score(name1 , name2):
    combined_names = (name1 + name2).lower()
    true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
    love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
    final_digit = int(str(true_count) + str(love_count))
    print(f"Your love score is {final_digit}")
calculate_love_score("Mohammed Reda", "Zainab Razak")



