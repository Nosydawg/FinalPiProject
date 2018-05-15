####################################################
# Names: Drake Weaver, Branson Hanzo, Daniel Munger
# Date: May 15th, 2018
# Description: Final Pi Project
####################################################

# import the necessary libraries
import Tkinter
import RPi.GPIO as GPIO
import time
import pygame

# functions to move the robot

# left turn
def leftTurn(event):
    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    left = GPIO.PWM(19,50)
    right = GPIO.PWM(18,100)
    left.start(0)
    right.start(10)
    time.sleep(1.5)
    left.start(10)
    time.sleep(1)

# right turn
def rightTurn(event):
    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    left = GPIO.PWM(19,50)
    right = GPIO.PWM(18,100)
    right.start(0)
    left.start(10)
    time.sleep(1.5)
    right.start(10)
    time.sleep(1)

# forward
def forward(event):
    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    left = GPIO.PWM(19,50)
    right = GPIO.PWM(18,100)
    left.start(0)
    right.start(0)
    left.ChangeDutyCycle(10)
    right.ChangeDutyCycle(10)
    time.sleep(2)

# backward
def backward(event):
    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    left = GPIO.PWM(19,50)
    right = GPIO.PWM(18,100)
    left.start(5)
    right.start(30)
    time.sleep(2)


#########################################################################################

# set the width and height of the tkinter canvas
WIDTH = 600
HEIGHT = 520

# create the window
window = Tkinter.Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
w = Tkinter.Canvas(window)

# create buttons for the GUI
up = Tkinter.Button(text = "FORWARD", padx = 5, pady = 5, command = forward)
left = Tkinter.Button(text = "LEFT", padx = 5, pady = 5, command = leftTurn)
right = Tkinter.Button(text = "RIGHT", padx = 5, pady = 5, command = rightTurn)
down = Tkinter.Button(text = "BACKWARD", padx = 5, pady = 5, command = backward)
robot = Tkinter.Label(text = "Robot", padx = 5, pady = 5, bg = "red")
up.grid(row = 0, column = 1)
left.grid(row = 1, column = 0)
right.grid(row = 1, column = 2)
down.grid(row = 2, column = 1)
robot.grid(row = 1, column = 1)

# assign the keys to the robot functions
window.bind('w', forward)
window.bind('a', leftTurn)
window.bind('s', backward)
window.bind('d', rightTurn)

window.mainloop()
GPIO.cleanup()
