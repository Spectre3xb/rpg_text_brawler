import random
import subprocess
import os

from player import Player
from enemies import Enemy


weapon_dict = {
    0 : ("Fists", 10),
    1 : ("Vibro Knife", 20),
    2 : ("Blaster Pistol", 30),
    3 : ("Type II Phaser", 45),
    4 : ("Vibroblade", 60),
    5 : ("Bat'leth", 75),
    6 : ("Blaster Rifle", 100),
    7 : ("Type III Phaser", 150),
    8 : ("Disruptor", 250),
    9 : ("Lightsaber", 500)
}

enemy_list = [
    ("Stormtrooper", 2, 20, 200, 2),
    ("Redshirt", 4, 4, 300, 3),
    ("War Droid", 6, 6, 400, 4)
]

def clear_screen():
    subprocess.call("cls" if os.name == "nt" else "clear", shell = True)


def initialize_player():
    name = input("Hello there. Would you care to tell me your name? ")
    clear_screen()
    return name

def print_stats(player):
    print(f"{player.name} current stats:")
    print(f"Attack: {player.attack}")
    print(f"Defense: {player.defense}")
    print(f"Constitution: {player.cons}")
    print(f"Weapon Proficiency: {player.prof}")
    print(f"HP: {player.hp}")


def intro():
    print("""
    Welcome to SciFi RPG Text Brawler!
    In this game you will first give your name, then allocate some stats, as per usual in an RPG.
    Afterwards you will be directly thrown into battle against your first foe. Combat is turn based.
    You will level up after every battle. Each level up will give you the opportunity to increase a stat by 5.
    Also you will get a certain amount of credits, which you can use to buy new weapons in the shop. 
    If you can defeat the final enemy, you will be crowned the new Emperor of the Galaxy!
    """)

def calculate_damage(weapon_base_damage):
    return weapon_base_damage + random.randint(1, 20)

def hit(proficiency, difficulty):
    return proficiency * random.randint(1, 20) > difficulty * 10

def your_turn(player, opponent):
    clear_screen()
    print(f"Your opponent is {opponent.name}, {opponent.hp} HP, {opponent.defense} defense.")
    print(f"Your HP is: {player.hp}")
    print("Your choice of weapons:")
    for weapon in player.weapons:
        print(f"[ {weapon} ] {weapon_dict[weapon][0]}")
    while True:
        try:
            weapon_choice = int(input(">"))
            if weapon_choice in player.weapons:
                break
            print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")
    if hit(player.prof, weapon_choice):
        print("Your hit landed")
        damage = calculate_damage(weapon_dict[weapon_choice][1]) - opponent.defense
        if damage < 0:
            damage = 0
        opponent.damage(damage)
        print(f"{opponent.name} has taken {damage} damage.")
        print(f"{opponent.name} has {opponent.hp} HP left.")
        input("Press ENTER to continue...")
    else:
        print("You hit yourself")
        damage = calculate_damage(weapon_dict[weapon_choice][1]) - player.defense
        if damage < 0:
            damage = 0
        player.damage(damage)
        print(f"You have taken {damage} damage.")
        print(f"{player.name} has {player.hp} HP left.")
        input("Press ENTER to continue...")


def opponent_turn(player, opponent):
    clear_screen()
    print(f"{opponent.name} is attacking!")
    print(f"Your HP is: {player.hp}")
    input("Press ENTER to see the attack...")

    weapon_choice = min(opponent.prof, 9)

    if hit(opponent.prof, weapon_choice):
        print(f"{opponent.name}'s attack landed!")
        damage = calculate_damage(weapon_dict[weapon_choice][1]) - player.defense
        if damage < 0:
            damage = 0
        player.damage(damage)
        print(f"You have taken {damage} damage.")
        print(f"You have {player.hp} HP left.")
        input("Press ENTER to continue...")
    else:
        print(f"{opponent.name} hit themselves in confusion!")
        damage = calculate_damage(weapon_dict[weapon_choice][1]) - opponent.defense
        if damage < 0:
            damage = 0
        opponent.damage(damage)
        print(f"{opponent.name} has taken {damage} damage.")
        print(f"{opponent.name} has {opponent.hp} HP left.")
        input("Press ENTER to continue...")


def fight(player, opponent):
    while opponent.hp > 0:
        your_turn(player, opponent)
        if opponent.hp <= 0:
            break
        opponent_turn(player, opponent)
        if player.hp <= 0:
            return
    player.level_up()
    clear_screen()
    print_stats(player)
    input("Press ENTER to continue...")





def main():
    clear_screen()
    intro()
    input("Press ENTER to continue...")
    clear_screen()
    player = Player(initialize_player(), attack = 5, defense = 5, cons = 5, prof = 5, weapons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print_stats(player)
    input("Press ENTER to continue...")
    clear_screen()
    for enemy in enemy_list:
        opponent = Enemy(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4])
        fight(player, opponent)
        if player.hp <= 0:
            break
    print("Game Over")


if __name__ == "__main__":
    main ()