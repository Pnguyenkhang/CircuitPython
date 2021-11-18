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
import pulseio

# pulse width modulation
led = pulseio.PWMOut(board.D3)

# change duty cycle value
def change_duty_cycle(led, pin):
    led.duty_cycle = pin.value

# Button 4 gets analog input voltage
analog_in = AnalogIn(board.D2)


# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# one pixel connected internally
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)



while True:
    try:
        print('voltage:    ',getVoltage(analog_in))
        change_duty_cycle(led, analog_in)
        time.sleep(0.5)
        print('duty cycle: ',analog_in.value)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
