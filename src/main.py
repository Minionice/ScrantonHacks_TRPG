#!/usr/bin/env python3

from player import Player

def main():
    print("Welcome.")
    print("What is your name?")
    name = None
    while name == None:
        name = input()
    player = Player(name)

if __name__ == "__main__":
    main()

