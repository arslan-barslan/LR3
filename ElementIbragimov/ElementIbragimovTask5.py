class ElementIbragimov():
	def __init__(self, name, symbol,number):
		self.name = name
		self.symbol = symbol
		self.number = number 
	def dump(self):
		print("Name",self.name," symbol ",self.symbol," number ",self.number)
elementik=ElementIbragimov('Углерод','C',6)
elementik.dump()


