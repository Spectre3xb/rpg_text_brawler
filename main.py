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
    ("Stormtrooper", 2, 2, 200, 2),
    ("Redshirt", 4, 4, 300, 3)
]

def clear_screen():
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)


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


def play(player, opponent):
    while opponent.hp > 0:
        clear_screen()
        print(f"Your opponent is {opponent.name}, {opponent.hp} HP")
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
        weapon_base_damage = weapon_dict[weapon_choice][1]
        damage = calculate_damage(weapon_base_damage)
        opponent.damage(damage)
        print(f"{opponent.name} has taken {damage} damage.")
        print(f"{opponent.name} has {opponent.hp} HP left.")
        input("Press ENTER to continue...")




def main():
    clear_screen()
    intro()
    input("Press ENTER to continue...")
    clear_screen()
    player = Player(initialize_player(), attack = 5, defense = 5, cons = 5, prof = 5, weapons = [0, 1, 5, 7, 8, 9])
    print_stats(player)
    input("Press ENTER to continue...")
    clear_screen()
    for enemy in enemy_list:
        opponent = Enemy(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4])
        play(player, opponent)



main ()