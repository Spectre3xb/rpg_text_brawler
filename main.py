import random
import subprocess
import os
from player import Player


game = True
weapon_dict = {
    1 : ("Fists", 10, 0),
    2 : ("Vibro Knife", 20, 50),
    3 : ("Blaster Pistol", 30, 100),
    4 : ("Type II Phaser", 45, 150),
    5 : ("Vibroblade", 60, 175),
    6 : ("Bat'leth", 75, 200),
    7 : ("Blaster Rifle", 100, 250),
    8 : ("Type III Phaser", 150, 300),
    9 : ("Lightsaber", 500, 1000)
}

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


def main():
    intro()
    input("Press ENTER to continue...")
    clear_screen()
    player = Player(initialize_player(), attack = 5, defense = 5, cons = 5, prof = 5)
    print_stats(player)


main ()