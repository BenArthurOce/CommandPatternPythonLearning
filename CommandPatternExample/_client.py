"The Command Pattern Use Case Example. A smart light Switch"
from ben_receiver import BenReceiver
from bensDad_Invoker import BensDadInvoker
from command_door_open import CommandDoorOpen
from command_door_close import CommandDoorClose
from command_end_code import CommandEndCode
from command_get_beer import CommandGetBeer
from command_get_onion import CommandGetOnion
from command_get_soda import CommandGetSoda
from data_fridge import Fridge

TheFridge = Fridge(iBeers=6, iOnions=10, iSodas=8)

# Create a receiver
Ben = BenReceiver()

# Create Commands
OPEN_DOOR = CommandDoorOpen(Ben, TheFridge)
CLOSE_DOOR = CommandDoorClose(Ben, TheFridge)
GET_BEER = CommandGetBeer(Ben, TheFridge)
GET_ONION = CommandGetOnion(Ben, TheFridge)
GET_SODA = CommandGetSoda(Ben, TheFridge)
END_CODE = CommandEndCode(Ben, TheFridge)

# Register the commands with the invoker
BensDad = BensDadInvoker()
BensDad.register("Open",OPEN_DOOR)
BensDad.register("Close",CLOSE_DOOR)
BensDad.register("Beer",GET_BEER)
BensDad.register("Onion",GET_ONION)
BensDad.register("Soda",GET_SODA)
BensDad.register("End",END_CODE)

# Execute the commands that are registered on the Invoker

code_is_complete = False

while code_is_complete == False:

    # Print Fridge Display
    #===========================
    fridge_display = (
    '                         \n'  
    ' =====================   \n'     
    ' │ The Fridge:       │   \n'
    ' │ Open? {0:5}       │   \n'
    ' │                   │   \n'
    ' │                   │   \n'
    ' │ BEERS:  {1}       │   \n'
    ' │ ONIONS: {2}       │   \n'
    ' │ SODAS:  {3}       │   \n'
    ' =====================   \n'
    '                         \n'
    ).format(
             format(bool(TheFridge.boolDoorOpen))
            ,format(TheFridge.iBeers, ' <3')
            ,format(TheFridge.iOnions, ' <3')
            ,format(TheFridge.iSodas, ' <3')
        )
    print(fridge_display)


    # Request User Input
    #===========================
    command_message = (
    ' Input  │ Action                       \n'
    '=========================              \n'
    ' Open:  │ Opens Fridge Door            \n'
    ' Close: │ Closes Fridge Door           \n'
    ' Beer:  │ Takes One Beer from Fridge   \n'
    ' Onion: │ Takes One Onion from Fridge  \n'
    ' Soda:  │ Takes One Soda from Fridge   \n'
    ' End:   │ Finishes taking items        \n'
    '                                       \n'
    ' Type Input Below:                     \n'
    )

    user_input = input(command_message)
    BensDad.execute(user_input.title())
