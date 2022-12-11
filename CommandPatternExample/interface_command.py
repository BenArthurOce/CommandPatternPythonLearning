"The switch interface, that all commands will implement"
from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "The switch interface, that all commands will implement"

    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"