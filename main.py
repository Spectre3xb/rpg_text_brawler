import random
import subprocess
import os
from player import Player

game = True

def clear_screen():
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)


def intro():
    print("""
    Welcome to Fantasy Text Brawler!
    In this game you will first give your name, then allocate some stats, as per usual in an RPG.
    Afterwards you will be directly thrown into battle against your first foe. Combat is turn based.
    You will level up after every battle. Each level up will give you a choice: Either a new weapon or increase a stat.
    If you can defeat the final enemy, you will be crowned the new Emperor of the Galaxy!
    """)


def main():
    intro()
    input("Press ENTER to continue...")
    clear_screen()

main ()