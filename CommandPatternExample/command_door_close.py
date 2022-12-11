from interface_command import ICommand

class CommandDoorClose(ICommand):
    def __init__(self, receiver, obj):
        self._receiver = receiver
        self._obj = obj

    def execute(self, *obj):
        self._receiver.run_command_DoorClose(self._obj)   