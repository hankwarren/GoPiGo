#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)

pwm.start(7.5)

try:
	dx = 12.0 / 180.0
	while True:
		for dc in range(2, 14, 1):
			print('change {}'.format(dc))
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.2)
		for dc in range(14, 2, -1):
			print('change {}'.format(dc))
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.2)
		dc = 2
		for i in range(0,180):
			dc += dx
			print('change {0:0.2f}'.format(dc))
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for i in range(0,180):
			dc -= dx
			print('change {0:0.2f}'.format(dc))
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.1)

#		print('change 2.5')
#		pwm.ChangeDutyCycle(2.5)
#		time.sleep(5)
#		print('change 12.5')
#		pwm.ChangeDutyCycle(12.5)
#		time.sleep(5)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
	print('program done')
