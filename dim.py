#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 50)		# channel=12, frequency=50
pwm.start(0)

try:
	while True:
		for dc in range(0, 101, 5):
			print('dim to {}'.format(dc))
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.5)
		for dc in range(100, -1, -5):
			print('dim to {}'.format(dc))
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.5)
except KeyboardInterrupt:
	pass

print('program done')
pwm.stop()
GPIO.cleanup()
