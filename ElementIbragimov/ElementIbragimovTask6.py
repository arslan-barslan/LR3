class ElementIbragimov():
	def __init__(self, name, symbol,number):
		self.name = name
		self.symbol = symbol
		self.number = number 
	def dump(self):
		print("Name",self.name," symbol ",self.symbol," number ",self.number)
	@property
	def get_name(self):
		return self.name
	@property
	def get_symbol(self):
		return self.symbol
	@property
	def get_number(self):
		return self.number





elementik=ElementIbragimov('Углерод','C',6)
elementik.dump()
print(elementik.get_name)
print(elementik.get_symbol)
print(elementik.get_number)
