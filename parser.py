import xml.dom.minidom
import re
from svg.path import parse_path
from objects import parse_line, parse_arc, parse_cubic_bezier

InFileName = 'owl.svg'
OutFileName = 'owl.hpql'

InFile = open(InFileName, 'r')
OutFile = open(OutFileName, 'w')

doc = xml.dom.minidom.parse(InFileName)
path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
	
output = 'ST0;\nU0,0;\nLED255,64,0;\n';

for input in path_strings:

	delimiter = "z"
	splits = re.split('z|Z', input)
	scale = 0.5;
	xoffset = 0.0;
	yoffset = 2500;

	for text in splits:
		if(text!=''):
			text += delimiter
		path = parse_path(text)
		
		counter = 0;
		for item in path:
			direction = "U"
			if(counter==0):
				direction = "U"
			else:
				direction = "D"
			
			if(str(type(item)) == "<class 'svg.path.path.Line'>"):
				output += parse_line(item, direction, scale, xoffset, yoffset)
			elif(str(type(item)) == "<class 'svg.path.path.Arc'>"):
				output += parse_arc(item, direction, scale, xoffset, yoffset)
			elif(str(type(item)) == "<class 'svg.path.path.CubicBezier'>"):
				output += parse_cubic_bezier(item, direction, scale, xoffset, yoffset)
				
			counter += 1

output += 'ST0;\nU0,0;\nLED128,128,128;\n';


OutFile.write(output)
OutFile.close() 
