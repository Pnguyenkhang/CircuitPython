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
import adafruit_hcsr04

# Sonar
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D2)

# Button 3
button3 = DigitalInOut(board.D3)
button3.direction = Direction.OUTPUT
button3.value = False

# Button 0
button0 = DigitalInOut(board.D0)
button0.direction = Direction.OUTPUT
button0.value = False

# Button 1
button1 = DigitalInOut(board.D1)
button1.direction = Direction.OUTPUT
button1.value = False
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



# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# one pixel connected internally
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)


offset = 5
minimum = 15
maximum = 30

while True:
    try:
        print((sonar.distance,))
        # green
        if sonar.distance >= minimum and sonar.distance <= maximum:
            button3.value = True
            button1.value = False
            button0.value = False
            print(button3.value)
            print("green on")
        # red
        elif (sonar.distance >= (minimum - offset) and sonar.distance < minimum) or (sonar.distance <= (maximum + offset) and sonar.distance > maximum):
            button1.value = True
            button0.value = False
            button3.value = False
            print("red on")

        elif sonar.distance > (maximum + offset) or sonar.distance < (minimum - offset) :
            button0.value = True
            button1.value = False
            button3.value = False
            print("Yellow on")
        else:
            print((sonar.distance,))
            button1.value = False
            button0.value = False
            button3.value = False
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
