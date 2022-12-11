import sys

#RECEIVER
#====================================
class BenReceiver():

    @staticmethod
    def run_command_DoorClose(TheFridge):
        TheFridge.boolDoorOpen = False

    @staticmethod
    def run_command_DoorOpen(TheFridge):
        TheFridge.boolDoorOpen = True

    @staticmethod
    def run_command_GetBeer(TheFridge):
        if TheFridge.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif TheFridge.iBeers == 0:
            input("\n There are no more beers left to take! \n Type any input to continue")
        else:
            TheFridge.iBeers -= 1   

    @staticmethod
    def run_command_GetOnion(TheFridge):
        if TheFridge.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif TheFridge.iOnions == 0:
            input("\n There are no more onions left to take! \n Type any input to continue")
        else:
            TheFridge.iOnions -= 1

    @staticmethod
    def run_command_GetSoda(TheFridge):
        if TheFridge.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif TheFridge.iSodas == 0:
            input("\n There are no more sodas left to take! \n Type any input to continue")
        else:
            TheFridge.iSodas -= 1

    @staticmethod
    def run_command_EndCode(TheFridge):
        if TheFridge.boolDoorOpen == True:    
            input("\n Don't leave the fridge door open! \n Type any input to continue")
        elif TheFridge.boolDoorOpen == False: 
            input("\n Enjoy your things! \n Type any input to continue")
            exit()