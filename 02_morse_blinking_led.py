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
time_multiplyer = 2

def ledRepeat (duration, interval, repetitions):
    for n in range(repetitions):
        ledOn(duration)
        ledOff(interval)
def shortSignal(repetitions):
    ledRepeat(0.2*time_multiplyer,0.2*time_multiplyer,repetitions)
def longSignal(repetitions):
    ledRepeat(0.6*time_multiplyer,0.2*time_multiplyer,repetitions)
def letter_space():
    ledOff(0.6*time_multiplyer)
def word_space():
    ledOff(1.4*time_multiplyer)
# letter code
def letterA():
    print("A")
    shortSignal(1)
    longSignal(1)
    letter_space()
def letterB():
    print("B")
    longSignal(1)
    shortSignal(3)
    letter_space()
def letterC():
    print("C")
    longSignal(1)
    shortSignal(1)
    longSignal(1)
    shortSignal(1)
    letter_space()
def letterD():
    print("D")
    longSignal(1)
    shortSignal(2)
    letter_space()
def letterE():
    print("E")
    shortSignal(1)
    letter_space()
def letterF():
    print("F")
    shortSignal(2)
    longSignal(1)
    shortSignal(1)
    letter_space() 
def letterG():
    print("G")
    longSignal(2)
    shortSignal(1)
    letter_space()
def letterH():
    print("H")
    shortSignal(4)
    letter_space()
def letterI():
    print("I")
    shortSignal(2)
    letter_space()
def letterJ():
    print("J")
    shortSignal(1)
    longSignal(3)
    letter_space()
def letterK():
    print("K")
    longSignal(1)
    shortSignal(1)
    longSignal(1)
    letter_space()
def letterL():
    print("L")
    shortSignal(1)
    longSignal(1)
    shortSignal(2)
    letter_space() 
def letterM():
    print("M")
    longSignal(2)
    letter_space()
def letterN():
    print("N")
    longSignal(1)
    shortSignal(1)
    letter_space()
def letterO():
    print("O")
    longSignal(3)
    letter_space()
def letterP():
    print("P")
    shortSignal(1)
    longSignal(2)
    shortSignal(1)
    letter_space()
def letterQ():
    print("Q")
    longSignal(2)
    shortSignal(1)
    longSignal(1)
    letter_space()
def letterR():
    print("R")
    shortSignal(1)
    longSignal(1)
    shortSignal(1)
    letter_space()
def letterS():
    print("S")
    shortSignal(3)
    letter_space()
def letterT():
    print("T")
    shortSignal(1)
    letter_space()
def letterU():
    print("U")
    shortSignal(2)
    longSignal(1)
    letter_space()
def letterW():
    print("W")
    shortSignal(1)
    longSignal(2)
    letter_space()
def letterX():
    print("X")
    longSignal(1)
    shortSignal(2)
    longSignal(1)
    letter_space()
def letterY():
    print("Y")
    longSignal(1)
    shortSignal(1)
    longSignal(2)
    letter_space()

def letterZ():
    print("Z")
    longSignal(2)
    shortSignal(2)
    letter_space()

def loop():

    while True:
        letterP()
        letterO() 
        letterP()
        letterR()
        letterA() 
        letterW()
        letterI()
        letterO() 
        letterN() 
        letterE() 
        print("-------------------------------------------------------")
        word_space()
def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
