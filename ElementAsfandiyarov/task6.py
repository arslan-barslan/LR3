class ElementAsfandiyarov():
	def __init__(self, name, symbol, number):
                self.name = name
                self.symbol = symbol
                self.number = number
	
	def dump():
		print('name:', self.name)
		print('symbol:', self.symbol)
		print('number:', self.number)
	@property
	def getter_name(self):
		return self.name
	@property
        def getter_symbol(self):
        	return self.symbol
	@property
        def getter_number(self):
		return self.number
element = ElementAsfandiyarov('Водород', 'H', 1)
element.dump
