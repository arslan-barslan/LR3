class ElementYagafarov():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print("Имя", self.name)
        print("Символ", self.symbol)
        print("Число", self.number)

element=ElementYagafarov('Хром','Cr','24')
element.dump()


