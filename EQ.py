import RPi.GPIO as GPIO
import sys
import Flags
import HAL.HC_SR04 as HC_SR04
import requests
import time
import Flags

def read_Sensors():
    HC_SR04.setup_Usensors()
    print(Flags.MODE)

    gain = 0
    pre_gain = 0
    gain2 = 0
    pre_gain2 = 0

    while Flags.MODE == Flags.EQ_MODE:
    #while True:
        print("hola")

        # Read sensor 1
        d1 = int(HC_SR04.read_Usensor1())
        print(d1)
        if(d1 > 84 and d1 < 112):
            if d1 in range(84, 92, 1):
                gain = -20
            #elif d1 in range(90, 94, 1):
            #    gain = -10
            elif d1 in range(93, 102, 1):
                gain = 0
            #elif d1 in range(102, 106, 1):
            #    gain = 10
            elif d1 in range(103, 112, 1):
                gain = 20    
    
            if pre_gain != gain:
                 requests.get(url="http://" + Flags.IP + "/eq?band=1&gain=" + str(gain))
                 #time.sleep(0.5)
                 print("request - Dist = ", d1, " gain = ", gain)

            pre_gain = gain

        # Read sensor 2
        d2 = int(HC_SR04.read_Usensor2())
        print(d2)
        if(d2 > 84 and d2 < 112):
            if d2 in range(84, 92, 1):
                gain2 = -20
            #elif d2 in range(90, 94, 1):
            #    gain2 = -10
            elif d2 in range(93, 102, 1):
                gain2 = 0
            #elif d2 in range(102, 106, 1):
            #    gain2 = 10
            elif d2 in range(103, 112, 1):
                gain2 = 20    
    
            if pre_gain2 != gain2:
                 requests.get(url="http://" + Flags.IP + "/eq?band=3&gain=" + str(gain2))
                 #time.sleep(0.5)
                 print("request - Dist = ", d2, " gain = ", gain2)

            pre_gain2 = gain2  

        # Read sensor 3
        #d3 = HC_SR04.read_Usensor3()
        #if(d3 > 10 and d3 < 80):
        #    print(str(d3))  

        # Read sensor 4
        #d4 = HC_SR04.read_Usensor4()
        #if(d4 > 10 and d4 < 80):
        #    print(str(d4))   
        print("EQ Mode")

