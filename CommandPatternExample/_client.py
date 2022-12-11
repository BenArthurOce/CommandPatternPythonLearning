"The Command Pattern Use Case Example. A smart light Switch"
from ben_receiver import BenReceiver
from bensDad_Invoker import BensDadInvoker
from command_door_open import CommandDoorOpen
from command_door_close import CommandDoorClose
from command_get_beer import CommandGetBeer
from command_get_onion import CommandGetOnion
from command_get_soda import CommandGetSoda

# Create a receiver
Ben = BenReceiver()

# Create Commands
OPEN_DOOR = CommandDoorOpen(Ben)
CLOSE_DOOR = CommandDoorClose(Ben)
GET_BEER = CommandGetBeer(Ben)
GET_ONION = CommandGetOnion(Ben)
GET_SODA = CommandGetSoda(Ben)


# Register the commands with the invoker
BensDad = BensDadInvoker()
BensDad.register("Open",OPEN_DOOR)
BensDad.register("Close",CLOSE_DOOR)
BensDad.register("Beer",GET_BEER)
BensDad.register("Onion",GET_ONION)
BensDad.register("Soda",GET_SODA)

# Execute the commands that are registered on the Invoker
BensDad.execute("Beer")
BensDad.execute("Soda")




# show history
#BensDad.show_history()

# replay last two executed commands
#BensDad.replay_last(2)