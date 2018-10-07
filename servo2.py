#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)
delay_time = 0.1

while True:
	for i in range(0, 180, 1):
		duty = float(i) / 10.0 + 2.5
		pwm.ChangeDutyCycle(duty)
		time.sleep(delay_time)

	print("Change direction -1")

	for i in range(180, 0, -1):
		duty = float(i) / 10.0 + 2.5
		pwm.ChangeDutyCycle(duty)
		time.sleep(delay_time)
		
	print("Change direction 1")
