#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led
def ledOff(duration):
    #print (f"LED OFF for: {duration} sec.")
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(duration)
def ledOn(duration):
    #print (f"LED ON for: {duration} sec.")
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    GPIO.output(LedPin, GPIO.LOW)  
    time.sleep(duration)
def ledRepeat (duration, interval, repetitions):
    for n in range(repetitions):
        ledOn(duration)
        ledOff(duration)
def shortSignal(repetitions):
    ledRepeat(0.3,0.3,repetitions)
def longSignal(repetitions):
    ledRepeat(0.6,0.3,repetitions)
# letter code
def letterA():
    print("A")
    shortSignal(1)
    longSignal(1)
    ledOff(1)
def letterB():
    print("B")
    longSignal(1)
    shortSignal(3)
    ledOff(1)
def letterC():
    print("C")
    longSignal(1)
    shortSignal(1)
    longSignal(1)
    shortSignal(1)
    ledOff(1)
def letterD():
    print("D")
    longSignal(1)
    shortSignal(2)
    ledOff(1)
def letterI():
    shortSignal(2)
    ledOff(1)
def letterM():
    longSignal(2)
    ledOff(1)
def letterN():
    print("N")
    longSignal(1)
    shortSignal(1)
    ledOff(1)
def letterO():
    print("O")
    longSignal(3)
    ledOff(1)
def letterP():
    shortSignal(1)
    longSignal(2)
    shortSignal(1)
    ledOff(1)
def letterR():
    print("R")
    shortSignal(1)
    longSignal(1)
    shortSignal(1)
    ledOff(1)
def letterS():
    shortSignal(3)
    ledOff(1)
def letterW():
    shortSignal(1)
    longSignal(2)
    ledOff(1)
def letterZ():
    longSignal(2)
    shortSignal(2)
    ledOff(1)

def loop():

    while True:
        letterD()
        letterO() 
        letterB()
        letterR()
        letterA() 
        letterN()
        letterO()
        letterC() 
        print("-------------------------------------------------------")
        ledOff(3)
def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
