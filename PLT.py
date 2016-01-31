from Coord import Coord

class PLT:
	
	list = None

	scale = 1.0
	
	def __init__(self):
		self.list = []
	
	def append(self, item):
		self.list.append(item)
		
	def output(self):
		output = ''
		for item in self.list:
			output += item.output()
		return(output) 