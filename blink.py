#!/usr/bin/python
import RPi.GPIO as GPIO
import time

LedPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)	# numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.output(LedPin, GPIO.LOW)

def blink():
	while True:
		print "LED on"
		GPIO.output(LedPin, GPIO.HIGH)
		time.sleep(1)
		print "LED off"
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(1)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		blink()
	except KeyboardInterrupt:
		destroy()
