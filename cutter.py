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
	
	cutting_depth
	cutting_speed
	up_speed
	plunge_speed
	lift_speed
	
	current_tool
	
	def __init__(self):
		return
	
	def move(self, direction):
		next_x = self.current_x
		next_y = self.current_y
		
		if(direction=='N'):
			next_y = self.current_y + self.step_size;
		elif(direction=='S'):
			next_y = self.current_y - self.step_size;
		elif(direction=='E'):
			next_x = self.current_x + self.step_size;
		elif(direction=='W'):
			next_x = self.current_x - self.step_size;
		
		self.move(next_x, next_y)

	def move(self, x, y):
		next_x = self.current_x + x
		next_y = self.current_y + y
		if(next_x<0):
			next_x = 0
		elif(next_x>MAX_X):
			next_x = MAX_X
		
		if(next_y<0):
			next_y = 0
		elif(next_y>MAX_Y):
			next_y = MAX_Y
		
		command = self.command('U', next_x, next_y)
		response = self.send(command)
		if(response == 'OK;'):
			self.current_x = next_x;
			self.current_y = next_y;
	
	# build a pen up/down command
	def command(self, dir, x, y):
		output = dir + str(int(x)) +","+ str(int(y)) +";\n"
		return(output)
	
	# send a string to the serial port and read the response
	def send(self, command):
		ser = serial.Serial ("/dev/ttyAMA0")	# open the serial port
		ser.baudrate = BAUDRATE
		ser.write(command)
		response = ser.read();
		ser.close()
		return(response)
		