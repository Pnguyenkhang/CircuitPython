import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_dotstar as dotstar
import time
import neopixel
import digitalio


'''
# Button 1
button1 = DigitalInOut(board.D1)
button1.direction = Direction.OUTPUT
button1.value = False
'''
'''
# Built in LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
# Digital input with pullup on D4
button4 = DigitalInOut(board.D4)
button4.direction = Direction.OUTPUT
button3 = DigitalInOut(board.D3)
button3.direction = Direction.OUTPUT
'''

# Button 4
button4 = DigitalInOut(board.D4)
button4.direction = Direction.OUTPUT
button4.value = False

# Button 3
button3 = DigitalInOut(board.D3)
button3.direction = Direction.OUTPUT
button3.value = False

# Button 0
button0 = DigitalInOut(board.D0)
button0.direction = Direction.OUTPUT
button0.value = False


# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# one pixel connected internally
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)



while True:
    try:
        print(getVoltage(button3),3)
        print(getVoltage(button0),0)
        print(getVoltage(button4),4)
        # green
        button0.value = True
        button3.value = False
        button4.value = False
        time.sleep(0.5)
        # yellow
        print(getVoltage(button3),3)
        print(getVoltage(button0),0)
        print(getVoltage(button4),4)
        button0.value = False
        button3.value = True
        button4.value = False
        time.sleep(0.5)
        # red
        print(getVoltage(button3),3)
        print(getVoltage(button0),0)
        print(getVoltage(button4),4)
        button0.value = False
        button3.value = False
        button4.value = True
        time.sleep(0.5)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
