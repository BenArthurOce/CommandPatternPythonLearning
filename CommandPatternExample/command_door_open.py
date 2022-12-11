from interface_command import ICommand

class CommandDoorOpen(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_DoorOpen()    