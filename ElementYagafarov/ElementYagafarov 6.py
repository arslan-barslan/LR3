class ElementYagafarov():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print("Имя", self.name)
        print("Символ", self.symbol)
        print("Число", self.number)

    @property
    def name_6(self):
        return self.name
    
    @property
    def symbol_6(self):
        return self.symbol
    
    @property
    def number_6(self):
        return self.number

element=ElementYagafarov('Хром','Cr','24')
element.dump()
print("Задание 6")
print(element.name_6)
print(element.symbol_6)
print(element.number_6)
