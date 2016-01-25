import serial
from svg2plt import SVG2PLT
import json

class Cutter:
	# CONSTANTS
	MAX_X = 10000		# maximum distance on the X axis
	MAX_Y = 10000		# maximum distance on the Y axis
	BAUDRATE = 57600	# baudrate for the serial port comms

	# The current location of the head on the x, y axis
	current_x = 0
	current_y = 0
	
	step_size = 100		# the number of positions to move with user control
	
	passes = 1		# the number of times to cut the shape
	
	cutting_depth = None
	cutting_speed = None
	up_speed = None
	plunge_speed = None
	lift_speed = None
	
	current_tool = 0
	
	serial = None
	
	def __init__(self):
		self.serial = serial.Serial ("/dev/ttyAMA0", self.BAUDRATE, timeout=1)	# open the serial "/dev/ttyAMA0"
		self.home()
	
	def __del__(self):	
		self.serial.close()
	
	def home(self):
		self.current_x = 0
		self.current_y = 0
		self.move(self.current_x, self.current_y)
	
	def open_svg(self):
		svg_file = 'static/svg/pattern.svg'		# TODO: break out somewhere instead of hard coded!

		self.svg2plt = SVG2PLT()
		self.svg2plt.x_offset = self.current_x
		self.svg2plt.y_offset = self.current_y
		self.svg2plt.parse_file(svg_file)
		
		output = {"width":self.svg2plt.display_width,"height":self.svg2plt.display_height,"units":self.svg2plt.display_units}
		return(json.dumps(output))

	def save_plt(self):
		OutFile = open('out.hpgl', 'w')			# TODO: break out somewhere instead of hard coded!
		OutFile.write(self.svg2plt.plt)
		OutFile.close() 

	def cut_file(self):
		self.open_svg()
		#self.save_plt()
		
		lines = self.svg2plt.plt.splitlines()	
		for line in lines:
			self.send(line)
	
	def move_direction(self, direction):
		if(direction=='N'):
			self.move((self.step_size*-1), 0)
		elif(direction=='S'):
			self.move(self.step_size, 0)
		elif(direction=='E'):
			self.move(0, (self.step_size*-1))
		elif(direction=='W'):
			self.move(0, self.step_size)

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
	
	# build a pen up/down command
	def command(self, dir, x, y):
		output = dir + str(int(x)) +","+ str(int(y)) +";\n"
		return(output)
	
	# send a string to the serial port and read the response
	def send(self, command):
		response = self.serial.write(command)
		return(response)
	
			
		