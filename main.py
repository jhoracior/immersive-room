import sys
import signal
from HAL.Gesture_sensor import PAJ7620U2, PAJ_UP, PAJ_DOWN
import RPi.GPIO as GPIO
import EQ
import Flags
import requests
import HAL.IR as IR



def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

#def signal_handler1(sig, frame):
#    Flags.Position = input("Dime: ")


if __name__ == '__main__':
    
    # SETUP
    #g_sensor = PAJ7620U2()
    IR.setup_IRsensors()
    signal.signal(signal.SIGINT, signal_handler)
    #signal.signal(signal.SIGTSTP, signal_handler1)
    #signal.pause()

    #lights
    requests.put(url = "http://" + Flags.Hue_IP + "/api/" + Flags.dev_ID + "/lights/1/state", json = Flags.colors[Flags.track_idx])
    requests.put(url = "http://" + Flags.Hue_IP + "/api/" + Flags.dev_ID + "/lights/2/state", json = Flags.colors[Flags.track_idx])

    # INFINITE LOOP
    while True:

        # Check for mode change flag
        if Flags.MODE == Flags.EQ_MODE:
            EQ.read_Sensors()

        # Read Gesture sensor
        #if g_sensor == PAJ_UP:
        if Flags.Position == "UP":
            if Flags.track_idx > 0 and Flags.track_idx <= 3:
                print("Up\r\n")
                r = requests.get(url = "http://" + Flags.IP + "/up")
                Flags.track_idx = Flags.track_idx - 1
                requests.put(url = "http://" + Flags.Hue_IP + "/api/" + Flags.dev_ID + "/lights/1/state", json = Flags.colors[Flags.track_idx])
                requests.put(url = "http://" + Flags.Hue_IP + "/api/" + Flags.dev_ID + "/lights/2/state", json = Flags.colors[Flags.track_idx])
            Flags.Position = "Reset"

                
        #elif g_sensor == PAJ_DOWN:
        if Flags.Position == "DOWN":
            if Flags.track_idx >= 0 and Flags.track_idx < 3:
                print("Down\r\n")
                r = requests.get(url = "http://" + Flags.IP + "/down")
                Flags.track_idx = Flags.track_idx + 1
                requests.put(url = "http://" + Flags.Hue_IP + "/api/" + Flags.dev_ID + "/lights/1/state", json = Flags.colors[Flags.track_idx])
                requests.put(url = "http://" + Flags.Hue_IP + "/api/" + Flags.dev_ID + "/lights/2/state", json = Flags.colors[Flags.track_idx])
            Flags.Position = "Reset"
