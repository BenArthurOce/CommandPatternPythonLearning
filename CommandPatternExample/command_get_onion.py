from interface_command import ICommand

class CommandGetOnion(ICommand):
    def __init__(self, receiver, obj):
        self._receiver = receiver
        self._obj = obj

    def execute(self, *obj):
        self._receiver.run_command_GetOnion(self._obj)     