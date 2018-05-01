

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
q = GPIO.PWM(19,50)
p = GPIO.PWM(18,50)
p.start(10)
q.start(10)
time.sleep(5)
p.stop()
q.stop()
GPIO.cleanup()

