import time
import smbus
import Flags

#i2c address
PAJ7620U2_I2C_ADDRESS   = 0x73
#Register Bank Selection
PAJ_BANK_SELECT         = 0xEF          #Bank0== 0x00,Bank1== 0x01
#Register Bank 0
PAJ_SUSPEND             = 0x03      #I2C suspend command (write= 0x01Enter the suspended state)
PAJ_INT_FLAG1_MASK      = 0x41      #Gesture detection interrupt flag mask
PAJ_INT_FLAG2_MASK      = 0x42      #Gesture /PS detects interrupt flag mask
PAJ_INT_FLAG1           = 0x43      #Gesture detects interrupt flags
PAJ_INT_FLAG2           = 0x44      #Gesture /PS detects interrupt flags
PAJ_STATE               = 0x45      #Gesture detection status indicator (only in gesture detection mode)
PAJ_PS_HIGH_THRESHOLD   = 0x69      #PS hysteresis high threshold (only in proximity detection mode)
PAJ_PS_LOW_THRESHOLD    = 0x6A      #PS hysteretic low threshold (only effective in proximity detection mode)
PAJ_PS_APPROACH_STATE   = 0x6B      #PS approaching state, approaching = 1
PAJ_PS_DATA             = 0x6C      #PS 8-bit data (valid only in gesture detection mode)
PAJ_OBJ_BRIGHTNESS      = 0xB0      #Object brightness (maximum 255)
PAJ_OBJ_SIZE_L          = 0xB1      #Object size (low 8 bits)
PAJ_OBJ_SIZE_H          = 0xB2      #Object size (high 8 bits)
#Register Bank 1
PAJ_PS_GAIN             = 0x44      #PS Gain setting (only available in proximity detection mode)
PAJ_IDLE_S1_STEP_L      = 0x67      #Idle S1 step size, used to set S1, response coefficient (low 8 bits)
PAJ_IDLE_S1_STEP_H      = 0x68      #Idle S1 step size, used to set S1, response coefficient (high 8 bits)
PAJ_IDLE_S2_STEP_L      = 0x69      #Free S2 step size for setting S2, response factor (low 8 bits)
PAJ_IDLE_S2_STEP_H      = 0x6A      #Free S2 step size, used to set S2, response factor (high 8 bits)
PAJ_OPTOS1_TIME_L       = 0x6B      #OPtoS1 Step，The OPtoS1 time used to set the operation state to standby 1 (low 8 bits)
PAJ_OPTOS2_TIME_H       = 0x6C      #OPtoS1 Step，Use to set OPtoS1 runtime to standby 1 stateHigh 8 bits)
PAJ_S1TOS2_TIME_L       = 0x6D      #S1toS2 step，S1toS2 time used to set standby state 1to standby state 2 (low 8 bits)
PAJ_S1TOS2_TIME_H       = 0x6E      #S1toS2 step，Set the S1toS2 time in standby 1to 8 bits higher in standby 2)
PAJ_EN                  = 0x72      #Enable/Disable PAJ7620U2
#Gesture detection interrupt flag mask
PAJ_RIGHT               = 0x01 
PAJ_LEFT                = 0x02
PAJ_UP                  = 0x04 
PAJ_DOWN                = 0x08
PAJ_FORWARD             = 0x10 
PAJ_BACKWARD            = 0x20
PAJ_CLOCKWISE           = 0x40
PAJ_COUNT_CLOCKWISE     = 0x80
PAJ_WAVE                = 0x100

#Start up Init array
Init_Register_Array = (
    (0xEF,0x00), (0x37,0x07), (0x38,0x17), (0x39,0x06), (0x41,0x00),
    (0x42,0x00), (0x46,0x2D), (0x47,0x0F), (0x48,0x3C), (0x49,0x00),
    (0x4A,0x1E), (0x4C,0x20), (0x51,0x10), (0x5E,0x10), (0x60,0x27), 
    (0x80,0x42), (0x81,0x44), (0x82,0x04), (0x8B,0x01), (0x90,0x06),
    (0x95,0x0A), (0x96,0x0C), (0x97,0x05), (0x9A,0x14), (0x9C,0x3F),
    (0xA5,0x19), (0xCC,0x19), (0xCD,0x0B), (0xCE,0x13), (0xCF,0x64),
    (0xD0,0x21), (0xEF,0x01), (0x02,0x0F), (0x03,0x10), (0x04,0x02),
    (0x25,0x01), (0x27,0x39), (0x28,0x7F), (0x29,0x08), (0x3E,0xFF),
    (0x5E,0x3D), (0x65,0x96), (0x67,0x97), (0x69,0xCD), (0x6A,0x01),
    (0x6D,0x2C), (0x6E,0x01), (0x72,0x01), (0x73,0x35), (0x74,0x00),
    (0x77,0x01),
)
#Register init array
Init_PS_Array = (
    (0xEF,0x00), (0x41,0x00), (0x42,0x00), (0x48,0x3C), (0x49,0x00),
    (0x51,0x13), (0x83,0x20), (0x84,0x20), (0x85,0x00), (0x86,0x10),
    (0x87,0x00), (0x88,0x05), (0x89,0x18), (0x8A,0x10), (0x9f,0xf8),
    (0x69,0x96), (0x6A,0x02), (0xEF,0x01), (0x01,0x1E), (0x02,0x0F),
    (0x03,0x10), (0x04,0x02), (0x41,0x50), (0x43,0x34), (0x65,0xCE),
    (0x66,0x0B), (0x67,0xCE), (0x68,0x0B), (0x69,0xE9), (0x6A,0x05),
    (0x6B,0x50), (0x6C,0xC3), (0x6D,0x50), (0x6E,0xC3), (0x74,0x05),
)
#Gesture register init array
Init_Gesture_Array = (
    (0xEF,0x00), (0x41,0x00), (0x42,0x00), (0xEF,0x00),
    (0x48,0x3C), (0x49,0x00), (0x51,0x10), (0x83,0x20),
    (0x9F,0xF9), (0xEF,0x01), (0x01,0x1E), (0x02,0x0F),
    (0x03,0x10), (0x04,0x02), (0x41,0x40), (0x43,0x30),
    (0x65,0x96), (0x66,0x00), (0x67,0x97), (0x68,0x01),
    (0x69,0xCD), (0x6A,0x01), (0x6B,0xB0), (0x6C,0x04),
    (0x6D,0x2C), (0x6E,0x01), (0x74,0x00), (0xEF,0x00),
    (0x41,0xFF), (0x42,0x01),
)

class PAJ7620U2(object):
    
    def __init__(self,address=PAJ7620U2_I2C_ADDRESS):
        self._address = address
        self._bus = smbus.SMBus(1)
        time.sleep(0.5)

        if self._read_byte(0x00) == 0x20:
            print("\nGesture Sensor OK\n")
            for num in range(len(Init_Register_Array)):
                self._write_byte(Init_Register_Array[num][0],Init_Register_Array[num][1])
        else:
            print("\nGesture Sensor Error\n")

        self._write_byte(PAJ_BANK_SELECT, 0)
        for num in range(len(Init_Gesture_Array)):
                self._write_byte(Init_Gesture_Array[num][0],Init_Gesture_Array[num][1])

    def _read_byte(self,cmd):
        return self._bus.read_byte_data(self._address,cmd)
    
    def _read_u16(self,cmd):
        LSB = self._bus.read_byte_data(self._address,cmd)
        MSB = self._bus.read_byte_data(self._address,cmd+1)
        return (MSB << 8) + LSB

    def _write_byte(self,cmd,val):
        self._bus.write_byte_data(self._address,cmd,val)

    def check_gesture(self):
        return self._read_u16(PAJ_INT_FLAG1)
    