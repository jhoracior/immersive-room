import RPi.GPIO as GPIO
import time

TRIG_1 = 20 
ECHO_1 = 21 

TRIG_2 = 19
ECHO_2 = 26

TRIG_3 = 1
ECHO_3 = 1

TRIG_4 = 1
ECHO_4 = 1

def setup_Usensors():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(TRIG_1, GPIO.OUT) 
    GPIO.setup(ECHO_1, GPIO.IN)

    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(TRIG_2, GPIO.OUT) 
    GPIO.setup(ECHO_2, GPIO.IN) 

    '''GPIO.setmode(GPIO.BCM)     
    GPIO.setup(TRIG_3, GPIO.OUT) 
    GPIO.setup(ECHO_3, GPIO.IN) 

    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(TRIG_4, GPIO.OUT) 
    GPIO.setup(ECHO_4, GPIO.IN)  '''
# END setup_Usensors

def read_Usensor1():
    GPIO.output(TRIG_1, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(TRIG_1, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_1, GPIO.LOW)

    while GPIO.input(ECHO_1) != GPIO.HIGH:
        pulso_inicio = time.time()
        print("1.1")

    while GPIO.input(ECHO_1) != GPIO.LOW:
        pulso_fin = time.time()
        print("2.1")

    duracion = pulso_fin - pulso_inicio

    return (34300 * duracion)/2
# END read_Usensor1

def read_Usensor2():
    GPIO.output(TRIG_2, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(TRIG_2, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_2, GPIO.LOW)

    while GPIO.input(ECHO_2) != GPIO.HIGH:
        pulso_inicio = time.time()
        print("1")

    while GPIO.input(ECHO_2) != GPIO.LOW:
        pulso_fin = time.time()
        print("2")

    duracion = pulso_fin - pulso_inicio

    return (34300 * duracion)/2
# END read_Usensor2

'''def read_Usensor3():
    GPIO.output(TRIG_3, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(TRIG_3, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_3, GPIO.LOW)

    while GPIO.input(ECHO_3) != GPIO.HIGH:
        pulso_inicio = time.time()

    while GPIO.input(ECHO_3) != GPIO.LOW:
        pulso_fin = time.time()

    duracion = pulso_fin - pulso_inicio

    return (34300 * duracion)/2
# END read_Usensor3

def read_Usensor4():
    GPIO.output(TRIG_4, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(TRIG_4, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_4, GPIO.LOW)

    while GPIO.input(ECHO_4) != GPIO.HIGH:
        pulso_inicio = time.time()

    while GPIO.input(ECHO_4) != GPIO.LOW:
        pulso_fin = time.time()

    duracion = pulso_fin - pulso_inicio

    return (34300 * duracion)/2'''
# END read_Usensor4