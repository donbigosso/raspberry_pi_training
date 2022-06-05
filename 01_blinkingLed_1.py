#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led
def shortBlink():
    print ('LED SHORT')
    GPIO.output(LedPin, GPIO.LOW)  # led on
    time.sleep(0.3)
def longBlink():
    print ('LED LONG')
    GPIO.output(LedPin, GPIO.LOW)  # led on
    time.sleep(1)

def ledOff():
    print ('LED OFF')
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(0.3)
def ledOffLong():
    print ('LED OFF Long')
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(2)


def loop():

    while True:
        shortBlink()
        ledOff()
        shortBlink()
        ledOff()
        shortBlink()
        ledOff()
        longBlink()
        ledOff()
        longBlink()
        ledOff()
        longBlink()
        ledOff()
        shortBlink()
        ledOff()
        shortBlink()
        ledOff()
        shortBlink()
        ledOffLong()

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
