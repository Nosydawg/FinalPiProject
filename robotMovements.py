


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
left = GPIO.PWM(19,50)
right = GPIO.PWM(18,100)
right.start(0)
left.start(0)

# left turn
def leftTurn():    
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(10)
    time.sleep(1.3)
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)

# right turn
def rightTurn():    
    right.ChangeDutyCycle(0)
    left.ChangeDutyCycle(10)
    time.sleep(1.3)
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)

# forward
def forward():    
    left.ChangeDutyCycle(10)
    right.ChangeDutyCycle(10)
    time.sleep(1)
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)

# backward
def backward():    
    left.ChangeDutyCycle(5)
    right.ChangeDutyCycle(30)
    time.sleep(1)
    left.ChangeDutyCycle(0)
    right.ChangeDutyCycle(0)

leftTurn()
rightTurn()
forward()
backward()

GPIO.cleanup()

