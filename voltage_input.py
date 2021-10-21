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




# Button 4
analog_in = AnalogIn(board.A1)


# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# one pixel connected internally
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)



while True:
    try:
        print(getVoltage(analog_in))
        time.sleep(0.5)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
