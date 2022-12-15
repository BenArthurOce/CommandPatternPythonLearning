import os

from ben_receiver import BenReceiver
from bensDad_Invoker import BensDadInvoker
from command_door_open import CommandDoorOpen
from command_door_close import CommandDoorClose
#from command_end_code import CommandEndCode
from command_get_apple import CommandGetApple
from command_get_beer import CommandGetBeer
from command_get_lime import CommandGetLime
from command_get_onion import CommandGetOnion
from command_get_soda import CommandGetSoda
from data_fridge import Fridge
from data_cupboard import Cupboard

TheFridge = Fridge(sObjectName="Fridge", iBeers=6, iOnions=10, iSodas=8)
TheCupboard = Cupboard(sObjectName="Cupboard", iOnions=5, iApples=4, iLimes=7)

# Create a receiver
Ben = BenReceiver()

# Create Commands
OPEN_FRIDGE = CommandDoorOpen(Ben, TheFridge)
CLOSE_FRIDGE = CommandDoorOpen(Ben, TheFridge)
GET_BEER_FRIDGE = CommandGetBeer(Ben, TheFridge)
GET_ONION_FRIDGE = CommandGetOnion(Ben, TheFridge)
GET_SODA_FRIDGE = CommandGetSoda(Ben, TheFridge)

OPEN_CUPBOARD = CommandDoorOpen(Ben, TheCupboard)
CLOSE_CUPBOARD = CommandDoorClose(Ben, TheCupboard)
GET_ONION_CUPBOARD = CommandGetOnion(Ben, TheCupboard)
GET_APPLE_CUPBOARD = CommandGetApple(Ben, TheCupboard)
GET_LIME_CUPBOARD = CommandGetLime(Ben, TheCupboard)
#END_CODE = CommandEndCode(Ben, TheFridge) #not in use


# Register the commands with the invoker
BensDad = BensDadInvoker()
BensDad.register("OpenFridge",OPEN_FRIDGE)
BensDad.register("CloseFridge",CLOSE_FRIDGE)
BensDad.register("BeerFridge",GET_BEER_FRIDGE)
BensDad.register("OnionFridge",GET_ONION_FRIDGE)
BensDad.register("SodaFridge",GET_SODA_FRIDGE)

BensDad.register("OpenCupboard",OPEN_CUPBOARD)
BensDad.register("CloseCupboard",CLOSE_CUPBOARD)
BensDad.register("OnionCupboard",GET_ONION_CUPBOARD)
BensDad.register("AppleCupboard",GET_APPLE_CUPBOARD)
BensDad.register("LimeCupboard",GET_LIME_CUPBOARD)
# BensDad.register("End",END_CODE) #not in use


while True:

    # Print Display and Commands
    #===========================
    kitchen_display = (
     '                                                                                                        \n'         
    '                                                          Input          │ Action                        \n'  
    ' =====================    =====================           ====================                           \n'     
    ' │ The Fridge:       │    │ The Cupboard:     │           OpenFridge:    │  Opens Fridge                 \n'
    ' │ Open? {0:5}       │    │ Open? {4:5}       │           CloseFridge:   │  Closes Fridge                \n'
    ' │                   │    │                   │           BeerFridge:    │  Takes 1 Beer from Fridge     \n'
    ' │                   │    │                   │           OnionFridge:   │  Takes 1 Beer from Fridge     \n'
    ' │ BEERS:  {1}       │    │ ONIONS:  {5}      │           SodaFridge:    │  Takes 1 Beer from Fridge     \n'
    ' │ ONIONS: {2}       │    │ APPLES:  {6}      │                          │                               \n'
    ' │ SODAS:  {3}       │    │ LIMES:   {7}      │           OpenCupboard:  │  Opens Cupboard               \n'
    ' =====================    =====================           CloseCupboard: │  Closes Cupboard              \n'
    '                                                          OnionCupboard: │  Takes 1 Onion from Cupboard  \n'
    '                                                          AppleCupboard: │  Takes 1 Apple from Cupboard  \n'
    '                                                          LimeCupboard:  │  Takes 1 Lime from Cupboard   \n'
    '                                                                                                         \n'
    '  Type Input Below (Not Case Sensitive):                                                                 \n'
    '  (Manually Exit code to turn off - Exit Feature coming)                                                 \n'
    '                                                                                                         \n'
    ).format(
            #==Fridge Contents==
             format(bool(TheFridge.boolDoorOpen))
            ,format(TheFridge.iBeers, ' <3')
            ,format(TheFridge.iOnions, ' <3')
            ,format(TheFridge.iSodas, ' <3')

            #==Cupboard Contents==
            ,format(bool(TheCupboard.boolDoorOpen))
            ,format(TheCupboard.iOnions, ' <3')
            ,format(TheCupboard.iApples, ' <3')
            ,format(TheCupboard.iLimes, ' <3')
        )


    # Execute User Commands
    #===========================
    user_input = input(kitchen_display)     # Asks for user input
    BensDad.execute(user_input)             # Executes the user input
    os.system('cls||clear')                 # Resets the terminal window


