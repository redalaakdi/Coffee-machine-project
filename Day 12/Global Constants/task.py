import random

logo = '''╔══════════════════════════════════════════╗
║                                          ║
║        🐉 DRAGON SLAYER 🐉               ║
║                                          ║
║   ____                                   ║
║  |    \  _ __  __ _  __ _  ___  _ __    ║
║  | |) || '__|/ _` |/ _` |/ _ \| '_ \   ║
║  |____/ |_|  \__,_|\__, |\___/|_| |_|  ║
║                     |___/               ║
║        ⚔️  Can you slay the beast? ⚔️    ║
║                                          ║
╚══════════════════════════════════════════╝'''
print(logo)
player_hp = 100
dragon_hp = 120
attack_damage = [15,25]
shield_reduction = 50
special_move = [35,50]
miss_chance = 30
name = (input("What is your name?"))
print(f"Welcome {name} prepare to face the DRAGON SLAYER GAME")

shield_active = False
while player_hp > 0 and dragon_hp > 0:
    print(f"Your hp is {player_hp}")
    print(f"Dragon hp is {dragon_hp}")
    print("1.Attack", "2.Shield", "3.Special Move")
    player_choice = input("Choose your move: ")
    if player_choice == "1":
        damage = random.randint(attack_damage[0], attack_damage[1])
        dragon_hp -= damage
        print(f"You attacked the DRAGON for {damage} damage")
    elif player_choice == "2":
        shield_active = True
    elif player_choice == "3":
        if random.randint(1,100) <= miss_chance:
            print("Your Special Move missed!")
        else:
            move = (random.randint(special_move[0], special_move[1]))
            dragon_hp -= move
            print(f"You used special move for {move} damage!")

    dragon_attack = random.randint(10, 20)
    if shield_active:
        dragon_attack = dragon_attack // 2
        print(f"🛡️ Shield blocked half the damage!")
        shield_active = False
    player_hp -= dragon_attack
    print(f"🐉 The dragon attacked you for {dragon_attack} damage!")
if player_hp <= 0:
    print("Dragon took over ,You Died!")
elif dragon_hp <= 0:
    print("You beat the dragon, you win!")
