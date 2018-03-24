"""
Command-processor module.
"""

from .player import Player
from .room import Room


def read_cmd(cmd: list, room: Room, player: Player) -> bool:
    """
    :param cmd: A list of words fed into the game, forming a command.
    :param room:
    :param player:
    :returns: Is the game over?
    """
    if cmd[0] == "go":
        if len(cmd) < 2:
            cmd.append("")
        if cmd[1] == "north" or cmd[1] == "n":
            return False
        if cmd[1] == "south" or cmd[1] == "s":
            return False
        if cmd[1] == "east" or cmd[1] == "e":
            return False
        if cmd[1] == "west" or cmd[1] == "w":
            return False
        else:
            print("What direction?")
            return False
    if cmd[0] == "look":
        if len(cmd) < 2:
            cmd.append("")
        if cmd[1] in room.items:
            return False
        else:
            print(room.description)
            return False
    if cmd[0] == "take":
        if len(cmd) < 2:
            cmd.append("")
        if cmd[1] in room.items:
            return False
        else:
            print("Take what?")
            return False
    if cmd[0] == "use":
        if len(cmd) < 2:
            cmd.append("")
        if cmd[1] in player.inventory:
            return False
        else:
            print("use what?")
            return False
    if cmd[0] == "quit":
        return True
    else:
        print("I don't know what that means.")
        return False
