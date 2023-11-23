import RPi.GPIO as GPIO
import Dashboard as DB

IR_SENSOR_VOL1 = 23
IR_SENSOR_VOL2 = 24
IR_SENSOR_VOL3 = 25
IR_SENSOR_VOL4 = 8
IR_SENSOR_PAN1 = 1
IR_SENSOR_PAN2 = 1
IR_SENSOR_PAN3 = 1
IR_SENSOR_PAN4 = 1
IR_SENSOR_MUTE = 4
IR_SENSOR_SOLO = 18
IR_SENSOR_EQ = 17
UP_PIN = 3
DOWN_PIN = 2


def setup_IRsensors():

    # Setup IR sensor 9 - Mute Button
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_MUTE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IR_SENSOR_MUTE, GPIO.FALLING, 
                    callback=DB.mute_handler, bouncetime=100)

    # Setup IR sensor 10 - Solo Button
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_SOLO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IR_SENSOR_SOLO, GPIO.FALLING, 
                    callback=DB.solo_handler, bouncetime=100)

    # Setup IR sensor 11 - Mode Change Button
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_EQ, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IR_SENSOR_EQ, GPIO.FALLING, 
                    callback=DB.mode_handler, bouncetime=100)

    # Setup VOL1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_VOL1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IR_SENSOR_VOL1, GPIO.FALLING, 
                    callback=DB.s1_handler, bouncetime=100)

    # Setup VOL2
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_VOL2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IR_SENSOR_VOL2, GPIO.FALLING, 
                    callback=DB.s2_handler, bouncetime=100)

    # Setup VOL3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_VOL3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IR_SENSOR_VOL3, GPIO.FALLING, 
                    callback=DB.s3_handler, bouncetime=100)

    # Setup VOL4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_SENSOR_VOL4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IR_SENSOR_VOL4, GPIO.FALLING, 
                    callback=DB.s4_handler, bouncetime=100)

    # Setup UP_PIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(UP_PIN, GPIO.FALLING, 
                    callback=DB.up_handler, bouncetime=100)

    # Setup DOWN_PIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(DOWN_PIN, GPIO.FALLING, 
                    callback=DB.down_handler, bouncetime=100)