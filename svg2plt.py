import xml.dom.minidom
import re
from svg.path import parse_path

from PLT import PLT

class SVG2PLT:
	# the PLT object for operations and export
	plt = None
	
	# SVG path objects
	paths = None
	
	delimiter = 'z'		# path delimiter (mM -> zZ)
	
	divisions = 30.0 	# the number of point divisions on an element
	overcut = 0.2		# how much to overcut the next shape (TODO: units for now as percentage. could be a percentage of the line, could be mm?)	
	
	# real world display measurements
	unit = 0.01			# a unit value for the number of pixels per inch
	display_width = 0
	display_height = 0
	display_units = "in"
	
	def __init__(self):
		self.paths = []
		self.plt = PLT()
		
	# open a file with name 'filename', extract the path elements
	def load_file(self, filename):
		#read the svg doc as a DOM to extract the XML <path> element
		doc = xml.dom.minidom.parse(filename)
		
		# determine the ratio of each pixel to real world units
		svg = doc.getElementsByTagName('svg')[0]
		
		#get the units for this file
		height = svg.getAttribute('height')
		width = svg.getAttribute('width')
		if(height.find("in")!=-1):
			self.display_units = "in"
		elif(height.find("mm")!=-1):
			self.display_units = "mm"
		elif(height.find("cm")!=-1):
			self.display_units = "cm"
		elif(height.find("px")!=-1):
			self.display_units = "px"
			
		height = height.replace(self.display_units, "")
		width = width.replace(self.display_units, "")

		viewbox = svg.getAttribute('viewBox').rsplit(" ")
		self.unit = (float(width)/float(viewbox[2]) + float(height)/float(viewbox[3]))/2
		
		# extract the path elements
		path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
		
		# iterate over each path that is found
		for path_string in path_strings:
			# break up each path shape into the individual lines (mM -> zZ)
			lines = re.split('z|Z', path_string)

			for line in lines:
				if(len(line)>2):
					line += self.delimiter
					item = parse_path(line) 		# convert the string to a path using svg.path library
					self.paths.append(item)		

	# load the file
	def parse(self):
		for path in self.paths:
			self.parse_path(path)
			
			if(path.closed==True):
				self.parse_overcut(path)
		
	# parse a path 
	def parse_path(self, path):
		first = True
		for item in path:
			self.parse_item(item, first)
			if(first):
				first = False;

	# parse an item (line, cubic, quadratic bezier)
	def parse_item(self, item, first):	
		for i in range(0, int(self.divisions)):
			loc = i/self.divisions
			point = item.point(loc)
			
			if(first and i==0):
				self.plt.add_coord('U', point.real, point.imag)
			
			self.plt.add_coord('D', point.real, point.imag)

	# parse a the first item in a path for overcut (line, cubic, quadratic bezier)
	def parse_overcut(self, path):
		item = path[0]
		
		for i in range(0, int(self.divisions*self.overcut)):
			loc = i/self.divisions
			point = item.point(loc)
			self.plt.add_coord('D', point.real, point.imag)
