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


# Built in LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
# Capacitive touch on D3
touch = touchio.TouchIn(board.D3)
# Digital input with pullup on D4
button1 = DigitalInOut(board.D4)
button1.direction = Direction.INPUT
button1.pull = Pull.UP
button1_in = True

# one pixel connected internally
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

RequiredTimeInState = 10
TimeInState = 0
count = 0
prevState = False
currState = False
while True:
    while currState == prevState:
        currState = button1.value
        TimeInState += 1
    if currState and TimeInState > RequiredTimeInState:
        # Code to do when button first pressed
        count+=1
        print("Number of times pressed",count)
    else:
        if TimeInState > RequiredTimeInState:
            # Code to do when button released
            print("button released")
    prevState = currState
    TimeInState = 0
