
from datetime import datetime
import time

#INVOKE - REGISTERS, EXECUTES COMMANDS
#====================================
class BensDadInvoker:
    def __init__(self):
        self._commands = {}
        self._history = []

    #Store a Command in the Invoker
    def register(self, command_name, command):
        self._commands[command_name] = command

    #Execute a stored Command in the Invoker
    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((time.time(), command_name))
        else:
            print(f"Command [{command_name}] not recognised")

    #Replay the last n commands executed
    def replay_last(self, number_of_commands):
        "Replay the last N commands"
        commands = self._history[-number_of_commands:]
        for each_command in commands:
            #self._commands[command[1]].execute()
            self.execute(each_command[1])
            #or if you want to record these replays in history
            #self.execute(command[1])