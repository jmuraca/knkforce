class Cutter:
	# The current location of the head on the x, y axis
	current_x = 0
	current_y = 0
	
	cutting_depth
	cutting_speed
	up_speed
	plunge_speed
	lift_speed
	
	current_tool
	
	def move(self, axis, value):
		if(axis=='X'):
			self.move_x(value)
		elif(axis=='Y'):
			self.move_y(value)
	
	def move_x(self, value):
		next_x = self.current_x + value
		if(next_x<0):
			next_x = 0
		elif(next_x>MAX_X):
			next_x = MAX_X
		
		command = self.command('U', next_x, self.current_y)
		response = self.send(command)
		if(response == 'OK;'):
			self.current_x = next_x;
	
	def command(self, dir, x, y):
		output = dir + str(int(x)) +","+ str(int(y)) +";\n"
		return(output)