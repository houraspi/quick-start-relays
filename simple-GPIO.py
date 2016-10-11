import RPi.GPIO as GPIO
import time

# set how we are going to refer to the pins
GPIO.setmode(GPIO.BCM)

# remember the pins for each relay for convenience
RELAY_PINS = {1: 4, 2: 17, 3: 27, 4: 22}
PINS = list(RELAY_PINS.values())

# set up each of the relay pins as an output
GPIO.setup(PINS, GPIO.OUT)

# turn on by setting the output to True for a pin
print('Turn on relay 1!')
GPIO.output(RELAY_PINS[1], True)

time.sleep(10)

# turn off by setting the output to False for a pin
print('Turn off relay 1!')
GPIO.output(RELAY_PINS[1], False)

time.sleep(10)

# turn on multiple relays
print('Turn on all relays!')
GPIO.output(PINS, True)

time.sleep(10)

# turn off multiple relays
print('Turn off all relays!')
GPIO.output(PINS, False)

# release control of the GPIOs
GPIO.cleanup()
