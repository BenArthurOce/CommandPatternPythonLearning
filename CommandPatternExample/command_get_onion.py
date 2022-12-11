from interface_command import ICommand

class CommandGetOnion(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_GetOnion()    