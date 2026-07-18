def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# The loop goes through all numbers from 1 to 20 and checks
# the condition to apply the given instructions.
# 2. When is the function meant to print "You got it"?
#The function prints "You got it" when i equals 20.
# 3. What are your assumptions about the value of i?
# My assumption was that range(1, 20) includes 20, but it
# actually stops at 19 — the stop value is exclusive.