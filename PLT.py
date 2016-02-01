from Coord import Coord

class PLT:
	# the lines as a string to output
	output = None
	
	# a list of coord lines
	list = None

	# factors to transform and translate the shape
	scale = 1.0
	x_offset = 0.0
	y_offset = 0.0
	cutter_factor = 11.5;		# a value to translate pixels to cutter drawing units
	
	# PLT properties 
	min_x = 100000
	min_y = 100000
	max_x = 0
	max_y = 0
	width = 0
	height = 0

	def __init__(self):
		self.list = []
	
	def build(self):
		self.output = self.start()
		
		for coord in self.list:
			self.output += coord.output()
		
		self.output += self.end()
		
		return(self.output)
		
	def start(self):
		output = 'ST0;\n'
		output += "U"+str(int(self.x_offset))+","+str(int(self.y_offset))+";\n"
		output += 'LED255,64,0;\n'
		return(output)
	
	def end(self):
		output = 'ST0;\n'
		output += "U"+str(int(self.x_offset))+","+str(int(self.y_offset))+";\n"
		output += 'LED128,128,128;\n'
		return(output)
		
	def output(self):
		string = ''
		for coord in self.list:
			string += coord.output()
		return(string)
	
	# write the PLT list to a file
	def write_file(self, filename):
		file = open(filename, 'w')			# TODO: break out somewhere instead of hard coded!
		for coord in self.list:
			output = coord.output()
			file.write(output)
		file.close() 
		
	# calculate the if x, y are the bounding box
	def calc_bounding_box(self):	
		for coord in self.list:
			if(coord.x<self.min_x):
				self.min_x = coord.x
			if(coord.x>self.max_x):
				self.max_x = coord.x
				
			if(coord.y<self.min_y):
				self.min_y = coord.y
			if(coord.y>self.max_y):
				self.max_y = coord.y
		
		self.width = self.max_x - self.min_x
		self.height = self.max_y - self.min_y
		
		print(self.min_x, self.min_y, self.max_x, self.max_y, self.width, self.height)
				
				
	def add_coord(self, dir, x, y):
		coord = Coord(dir, x, y)
		self.append(coord)
	
	def append(self, coord):
		self.list.append(coord)
