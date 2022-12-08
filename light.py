import pyfirmata
import time


board = pyfirmata.Arduino('COM5')

def turnon(command):
    
    if "green" in command:
        board.digital[13].write(1)
        return "ok sir"

    elif "yellow" in command:
        board.digital[12].write(1)
        return "ok sir"

    elif "white" in command:
        board.digital[11].write(1)
        return "ok sir"

    elif "red" in command:
        board.digital[10].write(1)
        return "ok sir"
    
    elif "all lights" in command or "all light" in command:
         board.digital[13].write(1)
         board.digital[12].write(1)
         board.digital[11].write(1)
         board.digital[10].write(1)
         return "ok sir"
    
    else:
        return "please select correct command"


def turnoff(command):
    
    if "green" in command:
        board.digital[13].write(0)
        return "ok sir"

    elif "yellow" in command:
        board.digital[12].write(0)
        return "ok sir"

    elif "white" in command:
        board.digital[11].write(0)
        return "ok sir"

    elif "red" in command:
        board.digital[10].write(0)
        return "ok sir"        
    
    elif "all lights" in command or "all light" in command:
         board.digital[13].write(0)
         board.digital[12].write(0)
         board.digital[11].write(0)
         board.digital[10].write(0)
         return "ok sir"


    else:
        return "please select correct command"

