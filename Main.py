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
		
	
		