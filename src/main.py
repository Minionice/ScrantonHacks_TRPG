#!/usr/bin/env python3

from Player import player

def main():
    print("Welcome.")
    print("What is your name?")
    name = input()
    player = Player(name)

if __name__ == "__main__":
    main()

