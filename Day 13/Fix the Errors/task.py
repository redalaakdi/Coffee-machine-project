try:
    year = int(input("What year you born in? "))

except ValueError:
    print("Please enter a valid numerical value")
    year = int(input("What year you born in? "))

if year > 2000:
    print("You're a gen Z")