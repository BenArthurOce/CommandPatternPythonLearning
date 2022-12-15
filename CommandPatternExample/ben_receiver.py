import sys

#RECEIVER
#====================================
class BenReceiver():

    @staticmethod
    def run_command_DoorClose(object):
        object.boolDoorOpen = False

    @staticmethod
    def run_command_DoorOpen(object):
        object.boolDoorOpen = True

    @staticmethod
    def run_command_GetApple(object):
        if object.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif object.iApples == 0:
            input("\n There are no more beers left to take! \n Type any input to continue")
        else:
            object.iApples -= 1   

    @staticmethod
    def run_command_GetBeer(object):
        if object.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif object.iBeers == 0:
            input("\n There are no more beers left to take! \n Type any input to continue")
        else:
            object.iBeers -= 1   

    @staticmethod
    def run_command_GetLime(object):
        if object.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif object.iLimes == 0:
            input("\n There are no more beers left to take! \n Type any input to continue")
        else:
            object.iLimes -= 1   

    @staticmethod
    def run_command_GetOnion(object):
        if object.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif object.iOnions == 0:
            input("\n There are no more onions left to take! \n Type any input to continue")
        else:
            object.iOnions -= 1

    @staticmethod
    def run_command_GetSoda(object):
        if object.boolDoorOpen == False:    
            input("\n The Door Must Be Opened First \n Type any input to continue")
        elif object.iSodas == 0:
            input("\n There are no more sodas left to take! \n Type any input to continue")
        else:
            object.iSodas -= 1

    @staticmethod
    def run_command_EndCode(object):
        if object.boolDoorOpen == True:    
            input("\n Don't leave the fridge door open! \n Type any input to continue")
        elif object.boolDoorOpen == False: 
            input("\n Enjoy your things! \n Type any input to continue")
            exit()