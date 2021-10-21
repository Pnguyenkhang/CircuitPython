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




# input 0
analog_in_0 = AnalogIn(board.A1)

# input 2
analog_in_2 = AnalogIn(board.A2)

# input 1
analog_in_1 = AnalogIn(board.A0)

# input 3
analog_in_3 = AnalogIn(board.A3)

# output 4
output4 = DigitalInOut(board.D4)
output4.direction = Direction.OUTPUT

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# one pixel connected internally
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)



while True:
    try:
        print(getVoltage(analog_in_0))

        time.sleep(2)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
