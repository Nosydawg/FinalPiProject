import Tkinter
import RPi.GPIO as GPIO
import time

#functions all go up need to change values

def Up():
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
	pass
	
def Down():
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
	pass

def Left():
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
	pass

def Right():
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
	pass

def Stop():
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
	pass

#########################################################################################
	
WIDTH = 600
HEIGHT = 520

window = Tkinter.Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
w = Tkinter.Canvas(window)

up = Tkinter.Button(text = "UP", padx = 5, pady = 5, command = Up)
left = Tkinter.Button(text = "LEFT", padx = 5, pady = 5, command = Left)
right = Tkinter.Button(text = "RIGHT", padx = 5, pady = 5, command = Right)
down = Tkinter.Button(text = "DOWN", padx = 5, pady = 5, command = Down)
stop = Tkinter.Button(text = "STOP", padx = 5, pady = 5, command = Stop)
up.grid(row = 0, column = 1, sticky = "N+E+S+W")
left.grid(row = 1, column = 0)
right.grid(row = 1, column = 2)
down.grid(row = 2, column = 1)
stop.grid(row = 1, column = 1)

window.mainloop()

