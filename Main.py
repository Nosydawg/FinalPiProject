import RPi.GPIO as GPIO
import time


class Robot():
	def __init__(self, Mazes):
		self.Mazes = []
		
	def create_new_maze():
		# called with GUI
		pass
		
	def left():
		# write code for left turn add node to tree set data as L and store timer
		# call follow_wall()
		pass
		
	def right():
		# write code for right turn update node 
		pass
		
	def follow_wall():
		# follow left line when line disappears call left()
		# start timer in case of back_track
		# if both photoresistors read a wall stop timer and call back_track()
		# if finished call set_solution
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
		
	def backtrack():
		# drive in reverse until timer runs out
		# turn right drive forward if dead end right after call right 
		# update node either straight or right
		pass
		
	def set_solution():
		pass
		
class Maze():
	def __init__(self):
		self.solution = []
		
class tree():
	def __init__(self, decision):
		self.data = decision
		self.left = None
		self.right = None
		
		
		
	
		