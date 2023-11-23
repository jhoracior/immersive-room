import RPi.GPIO as GPIO
import time
import signal
import sys

# Stack para checar direccion de gestos en sensores
stack = []

def signal_handler(sig, frame):
    GPIO.cleanup()
    print("CTRL+C presionado")
    sys.exit(0)
                
def s1_handler(channel):
    print(stack)
    if not stack:
        stack.append(1)
    elif(len(stack) == 3 and stack[0] == 4 and stack[1] == 3 and stack[2] == 2):
         stack.clear()
         print("Vol = 0")

def s2_handler(channel):
    print(stack)
    if not stack:
       return 
    if ((len(stack) == 1 and stack[0] == 1) or (len(stack) == 2 and stack[0] == 4 and stack[1] == 3)):
        if (stack[-1] != 2):
            stack.append(2)     
            print("Vol = 33") 

def s3_handler(channel):
    print(stack)
    if not stack:
       return 
    if ((len(stack) == 1 and stack[0] == 4) or (len(stack) == 2 and stack[0] == 1 and stack [1] == 2)):
         if (stack[-1] != 3):
            stack.append(3)     
            print("Vol = 67") 

def s4_handler(channel):
    print(stack)
    if not stack:
        stack.append(4)
    elif(len(stack) == 3 and stack[0] == 1 and stack[1] == 2 and stack[2] == 3):
        stack.clear()
        print("Vol = 100")               

sensor01 = 17
sensor02 = 18
sensor03 = 27
sensor04 = 24

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor01, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sensor01, GPIO.FALLING, 
                    callback=s1_handler, bouncetime=100)
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor02, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sensor02, GPIO.FALLING, callback=s2_handler, bouncetime=100)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor03, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sensor03, GPIO.FALLING, callback=s3_handler, bouncetime=100)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor04, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sensor04, GPIO.FALLING, callback=s4_handler, bouncetime=100)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
