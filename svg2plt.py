import xml.dom.minidom
import re
from svg.path import parse_path

class SVG2PLT:
		
	# the plt code to output
	plt = ''
	
	# path delimiter (mM -> zZ)
	delimiter = 'z'

	# factors to transform the SVG as it is read
	scale = 1.0
	x_offset = 0.0
	y_offset = 0.0
	
	# the number of point divisions on an element
	steps = 30.0
	

	def start(self):
		self.plt += 'ST0;\nU0,0;\nLED255,64,0;\n'
	
	def end(self):
		self.plt += 'ST0;\nU0,0;\nLED128,128,128;\n'
		
	# open a file with name 'filename', extract the path elements, and convert them to PLT code
	def parse_file(self, filename):
		#read the svg doc as a DOM to extract the XML <path> element
		doc = xml.dom.minidom.parse(filename)
		path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
		
		# iterate over each path that is found
		for path_string in path_strings:
			# break up each path shape into the individual lines (mM -> zZ)
			lines = re.split('z|Z', path_string)

			for line in lines:
				if(line!=''):
					line += self.delimiter
				path = parse_path(line)
				
				self.parse_path(path)


		
	# parse a path (mM -> zZ)
	def parse_path(self, path):
		first = True
		for item in path:
			if(str(type(item)) == "<class 'svg.path.path.Line'>"):
				self.plt += self.parse_line(item, first)
			elif(str(type(item)) == "<class 'svg.path.path.Arc'>"):
				self.plt += self.parse_arc(item, first)
			elif(str(type(item)) == "<class 'svg.path.path.CubicBezier'>"):
				self.plt += self.parse_cubic_bezier(item, first)
			if(first):
				first = False;
	
	def parse_line(self, item, first):
		output = ''
		start = item.start
		end = item.end
		
		if(first):
			output += self.command('U', start.real, start.imag)
			output += self.command('D', start.real, start.imag)
			output += self.command('D', end.real, end.imag)
		else:
			output += self.command('D', end.real, end.imag)
			
		return output
		
	def parse_arc(self, item, first):
		output = ''
		
		for i in range(0, self.steps):
			loc = i/self.steps
			point = item.point(loc)
			
			if(first and i==0):
				output += self.command('U', point.real, point.imag)
			
			output += self.command('D', point.real, point.imag)
			
		return output
		
	def parse_cubic_bezier(self, item, first):
		output = ''
		
		for i in range(0, int(self.steps)):
			loc = i/self.steps
			point = item.point(loc)
			
			if(first and i==0):
				output += self.command('U', point.real, point.imag)
			
			output += self.command('D', point.real, point.imag)
			
		return output
		
	def command(self, dir, x, y):
		output = dir + str(int(x*self.scale+self.x_offset)) +","+ str(int(y*self.scale+self.y_offset)) +";\n"
		return(output)