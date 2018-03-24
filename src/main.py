#!/usr/bin/env python3

from src import command
from src import player
from src import room


def main():
    play = player.Player()
    done = False

    current_room = room.Room(True, False, False, False, "You are in a room.", [])

    while not done:
        done = command.read_cmd(input("> ").split(" "), current_room, play)


if __name__ == "__main__":
    main()
