

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
left = GPIO.PWM(19,50)
right = GPIO.PWM(18,100)
left.start(10)
right.start(10)
time.sleep(1)
left.stop()
right.stop()
GPIO.cleanup()

