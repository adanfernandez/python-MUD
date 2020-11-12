from collections import deque

class ReadFile:

    def __init__(self):
        self.commands = []

    def read_file(self, file: str):
        with open(file, "r") as lines:
            for i in lines:
                l = i.strip('\n')
                self.commands.append(l)
        self.commands.reverse()

    def get_command(self):
        if(len(self.commands) == 0):
            print("No hay más órdenes que ejecutar")
        else:
            return self.commands.pop()
