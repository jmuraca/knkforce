import serial

class Cutter:
	# CONSTANTS
	MAX_X = 10000		# maximum distance on the X axis
	MAX_Y = 10000		# maximum distance on the Y axis
	BAUDRATE = 57600	# baudrate for the serial port comms

	# The current location of the head on the x, y axis
	current_x = 0
	current_y = 0
	step_size = 100
	
	cutting_depth = None
	cutting_speed = None
	up_speed = None
	plunge_speed = None
	lift_speed = None
	
	current_tool = 0
	
	def __init__(self):
		self.current_x = 0
		self.current_y = 0
		self.move(self.current_x, self.current_y)
		return
	
	def move_direction(self, direction):
		if(direction=='N'):
			self.move(0, self.step_size)
		elif(direction=='S'):
			self.move(0, (self.step_size*-1))
		elif(direction=='E'):
			self.move(self.step_size, 0)
		elif(direction=='W'):
			self.move((self.step_size*-1), 0)

	def move(self, x, y):
		next_x = self.current_x + x
		next_y = self.current_y + y
		if(next_x<0):
			next_x = 0
		elif(next_x>self.MAX_X):
			next_x = self.MAX_X
		
		if(next_y<0):
			next_y = 0
		elif(next_y>self.MAX_Y):
			next_y = self.MAX_Y
		
		command = self.command('U', next_x, next_y)
		response = self.send(command)
		if(response):
			self.current_x = next_x;
			self.current_y = next_y;
		print(str(self.current_x)+","+str(self.current_y))
	
	# build a pen up/down command
	def command(self, dir, x, y):
		output = dir + str(int(x)) +","+ str(int(y)) +";\n"
		return(output)
	
	# send a string to the serial port and read the response
	def send(self, command):
		# ser = serial.Serial (0)	# open the serial  "/dev/ttyAMA0"
		# ser.baudrate = BAUDRATE
		# ser.write(command)
		# response = ser.read();
		# ser.close()
		response = "OK;"
		return(response)
		