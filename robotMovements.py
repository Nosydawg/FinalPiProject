


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
left = GPIO.PWM(19,50)
right = GPIO.PWM(18,100)

# left turn
left.stop()
right.start(10)
time.sleep(1.3)

# right turn
right.stop()
left.start(10)
time.sleep(1.3)

# forward
left.start(10)
right.start(10)

# backward
left.start(5)
right.start(30)

GPIO.cleanup()

