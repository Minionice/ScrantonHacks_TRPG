class CommandProcessor(object):
    def __init___(self):
        pass

    def read_cmd(self, cmd: list):
        """
        :param cmd: A list of words fed into the game, forming a command.
        """
        if cmd[0] is "go":
            if cmd[1] is "north":
                pass
            if cmd[1] is "south":
                pass
            if cmd[1] is "east":
                pass
            if cmd[1] is "west":
                pass
            else:
                print("What direction?")
        else:
            print("I don't know what that means.")
