class Conus():
        def __init__(self,radius,height):
                self.radius = radius
                self.height = height
        @property
        def radius(self):
                return self.radius
        @property
        def height(self):
                return self.height
    
        @height.setter
        def height(self, value):
                if value <= 0:
                        raise ValueError("Высота должна быть больше нуля, и не равнятся нулю")
                self.height = value
        
        @radius.setter
        def radius(self, value):
                if value <= 0:
                        raise ValueError("Радиус должен быть больше нуля, и не равнятся нулю")
                self.radius = value 
        
	
        @staticmethod
        def about():
                print("Данную работу сделали Ибрагимов А.А как разработчик №1, Ягафаров М.М как разработчик №2 и Асфандияров А.Р разработчик №3")
                
        def calc_volume(self):
                pass
