from adafruit_crickit import crickit
from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull

import time
import audioio
import board
import pulseio
import array
import math
import audiobusio
import board

# buttonA = DigitalInOut(board.BUTTON_A)
# buttonA.direction = Direction.INPUT
# buttonA.pull = Pull.DOWN
# ticker = 0
lumens = .01
color = 10
button_a_on = False

def startupLEDs(ticker):
    while ticker < 4:
        cpx.pixels.brightness = (ticker * lumens) + .01
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(1 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(1 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(1 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((ticker * 85, 255 - (ticker * 85), 0))
        time.sleep(.5 - ticker * .1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(2)
        ticker = ticker + 1


def lightUpLEDs():
    # The LEDs are *really* bright. Value is between 0.0 and 1.0 .
    cpx.pixels.brightness = 0.1
    cpx.pixels.fill((0xff, 0x30, 0x30))
    cpx.pixels[0] = (0xff, 0x01, 0x01)
    cpx.pixels[1] = (0x00, 0xff, 0x00)
    cpx.pixels[2] = (0x00, 0x00, 0xff)
    cpx.pixels[3] = (0x00, 0x00, 0x00)
    time.sleep(0.5)

def motorProgram():
    crickit.dc_motor_1.throttle = 0.8
    # Left
    crickit.dc_motor_2.throttle = 1.0
    time.sleep(4.0)
    crickit.dc_motor_1.throttle = 0.5
    crickit.dc_motor_2.throttle = 0.5
    time.sleep(1.0)
    crickit.dc_motor_1.throttle = -0.30
    crickit.dc_motor_2.throttle = 0.30
    time.sleep(1.0)
    crickit.dc_motor_1.throttle = 0.0
    crickit.dc_motor_2.throttle = 0.0

def playSoundFile():
    wavfile = "end_loop.wav"
    cpx.play_file(wavfile)

def servoProgram():
    crickit.continuous_servo_1.throttle = 1.0
    time.sleep(2)
    crickit.continuous_servo_1.throttle = 0.5
    time.sleep(2)
    crickit.continuous_servo_1.throttle = 0   # Stop
    time.sleep(2)
    crickit.continuous_servo_1.throttle = -0.5  #  Backwards halfspeed
    time.sleep(2)
    crickit.continuous_servo_1.throttle = -1  #  Forwards
    time.sleep(2)
    crickit.continuous_servo_1.throttle = 0   # Stop
    time.sleep(2)

def IRReader():
    ss = crickit.seesaw
    IR1 = crickit.SIGNAL1
    ss.pin_mode(IR1, ss.INPUT)

    while True:
        print((ss.analog_read(IR1),))
        time.sleep(0.025)

        infraredValue = ss.analog_read(IR1)
        ratio = infraredValue / 1025
        ledValue = int(ratio * 255)
        cpx.pixels[0] = (ledValue, 0, 125)
        cpx.pixels[1] = (ledValue, 50, 150)

def normalized_rms(values):
    minbuf = int(mean(values))
    return math.sqrt(sum(float((sample - minbuf) * (sample - minbuf)) for sample in values) / len(values))
def mean(values):
    return (sum(values) / len(values))

def microphoneRead():
    b = array.array("H")
    for i in range(200):
        b.append(0)
    with audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, bit_depth=16) as mic:
        mic.record(b, len(b))

    time.sleep(2)
    print(normalized_rms(b))

while True:
    # Start Program

    microphoneRead()
    if cpx.button_a:
        if button_a_on is False:
            button_a_on = True
            startupLEDs(0)
            servoProgram()
        else:
            button_a_on = False

elif cpx.button_b:
    cpx.pixels[5:10] = [(0, 255, 0)] * 5
    else:
        cpx.pixels.fill((0, 0, 0))



pass

