import Flags
import HAL.IR
import requests
import time

stack = []
mute_pressed = []
solo_pressed = []
mode_pressed = []

def mute_handler(channel):
    mute_pressed.append(1)
    if len(mute_pressed) < 2:
        requests.get(url = "http://" + Flags.IP + "/mute")
        print("Mute")
        time.sleep(0.5)
    if len(mute_pressed) >= 2:
        mute_pressed.clear()

def solo_handler(channel):
    solo_pressed.append(1)
    if len(solo_pressed) < 2:
        requests.get(url = "http://" + Flags.IP + "/solo")
        print("Solo")
        time.sleep(0.5)
    if len(solo_pressed) >= 2:
        solo_pressed.clear()

def mode_handler(channel):
    mode_pressed.append(1)
    if len(mode_pressed) < 2:
        Flags.MODE = not Flags.MODE 
        print("Change Mode")
        requests.get(url = "http://" + Flags.IP + "/eq_mode")
        time.sleep(0.5)
    if len(mode_pressed) >= 2:
        mode_pressed.clear()


def s1_handler(channel):
    print(stack)
    if not stack:
        stack.append(1)
    elif(len(stack) == 3 and stack[0] == 4 and stack[1] == 3 and stack[2] == 2):
         stack.clear()
         requests.get(url = "http://" + Flags.IP + "/vol?v=0&tn="+ str(Flags.track_idx))
         print("Vol = 0")

def s2_handler(channel):
    print(stack)
    if not stack:
       return 
    if ((len(stack) == 1 and stack[0] == 1) or (len(stack) == 2 and stack[0] == 4 and stack[1] == 3)):
        if (stack[-1] != 2):
            stack.append(2)     
            print("Vol = 33")
            requests.get(url = "http://" + Flags.IP + "/vol?v=33&tn="+ str(Flags.track_idx)) 

def s3_handler(channel):
    print(stack)
    if not stack:
       return 
    if ((len(stack) == 1 and stack[0] == 4) or (len(stack) == 2 and stack[0] == 1 and stack [1] == 2)):
         if (stack[-1] != 3):
            stack.append(3)     
            print("Vol = 67") 
            requests.get(url = "http://" + Flags.IP + "/vol?v=66&tn="+ str(Flags.track_idx))

def s4_handler(channel):
    print(stack)
    if not stack:
        stack.append(4)
    elif(len(stack) == 3 and stack[0] == 1 and stack[1] == 2 and stack[2] == 3):
        stack.clear()
        print("Vol = 100")
        requests.get(url = "http://" + Flags.IP + "/vol?v=100&tn="+ str(Flags.track_idx)) 

def up_handler(channel):
    print("UP")
    Flags.Position = "UP"

def down_handler(channel):
    print("DOWN")
    Flags.Position = "DOWN"


