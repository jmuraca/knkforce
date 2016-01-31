class Coord:
	cmd = 'U'
	x = 0.0
	y = 0.0

	def __init__(self, cmd, x, y):
		self.cmd = cmd
		self.x = float(x)
		self.y = float(y)
	
	def output(self):
		output = self.cmd+str(int(self.x))+","+str(int(self.y))+";\n"
		return(output)