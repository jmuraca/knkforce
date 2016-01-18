def parse_line(item, direction, scale, xoffset, yoffset):
	output = ''
	start = item.start
	end = item.end
	
	if(direction=="U"):
		output = "U"+str(int(start.real*scale+xoffset))+","+str(int(start.imag*scale+yoffset))+";"+"\n"
		output += "D"+str(int(start.real*scale+xoffset))+","+str(int(start.imag*scale+yoffset))+";"+"\n"
		output += "D"+str(int(end.real*scale+xoffset))+","+str(int(end.imag*scale+yoffset))+";"+"\n"
	else:
		output += "D"+str(int(end.real*scale+xoffset))+","+str(int(end.imag*scale+yoffset))+";"+"\n"
		
	return output
	
def parse_arc(item, direction, scale, xoffset, yoffset):
	output = ''
	for x in range(0, 30):
		loc = x/30.0
		point = item.point(loc)
		if(direction=="U" and x==0):
			output += "U"+str(int(point.real*scale+xoffset))+","+str(int(point.imag*scale+yoffset))+";"+"\n"
		output += "D"+str(int(point.real*scale+xoffset))+","+str(int(point.imag*scale+yoffset))+";"+"\n"
		
	return output
	
def parse_cubic_bezier(item, direction, scale, xoffset, yoffset):
	output = ''
	for x in range(0, 30):
		loc = x/30.0
		point = item.point(loc)
		if(direction=="U" and x==0):
			output += "U"+str(int(point.real*scale+xoffset))+","+str(int(point.imag*scale+yoffset))+";"+"\n"
		output += "D"+str(int(point.real*scale+xoffset))+","+str(int(point.imag*scale+yoffset))+";"+"\n"
		
	return output