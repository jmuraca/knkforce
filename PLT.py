from Coord import Coord

class PLT:
	
	list = None

	# factors to transform and translate the shape
	scale = 1.0
	x_offset = 0.0
	y_offset = 0.0

	def __init__(self):
		self.list = []
	
	def append(self, coord):
		self.list.append(coord)
		
	def add_coord(self, dir, x, y):
		coord = Coord(dir, x, y)
		self.append(coord)
		
	def start(self):
		self.plt += 'ST0;\n'
		self.plt += "U"+str(int(self.x_offset))+","+str(int(self.y_offset))+";\n"
		self.plt += 'LED255,64,0;\n'
	
	def end(self):
		self.plt += 'ST0;\n'
		self.plt += "U"+str(int(self.x_offset))+","+str(int(self.y_offset))+";\n"
		self.plt += 'LED128,128,128;\n'
		
	def output(self):
		output = ''
		for coord in self.list:
			output += coord.output()
		return(output) 