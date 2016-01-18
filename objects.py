def parse_line(item, direction):
	output = ''
	start = item.start
	end = item.end
	
	if(direction=="U"):
		output = "U"+str(int(start.real))+","+str(int(start.imag))+";"+"\n"
		output += "D"+str(int(start.real))+","+str(int(start.imag))+";"+"\n"
		output += "D"+str(int(end.real))+","+str(int(end.imag))+";"+"\n"
	else:
		output += "D"+str(int(end.real))+","+str(int(end.imag))+";"+"\n"
		
	return output
	
def parse_arc(item, direction):
	output = ''
	for x in range(0, 30):
		loc = x/30.0
		point = item.point(loc)
		if(direction=="U" and x==0):
			output += "U"+str(int(point.real))+","+str(int(point.imag))+";"+"\n"
		output += "D"+str(int(point.real))+","+str(int(point.imag))+";"+"\n"
		
	return output
	
def parse_cubic_bezier(item, direction):
	output = ''
	for x in range(0, 30):
		loc = x/30.0
		point = item.point(loc)
		if(direction=="U" and x==0):
			output += "U"+str(int(point.real))+","+str(int(point.imag))+";"+"\n"
		output += "D"+str(int(point.real))+","+str(int(point.imag))+";"+"\n"
		
	return output