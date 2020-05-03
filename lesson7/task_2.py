from abc import ABC, abstractmethod

class Clothes(ABC):
    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def param(self) -> int:
        pass

    @abstractmethod
    def fabric_consumption(self) -> float:
        pass

class Coat(Clothes):
        def __init__(self, size):
            self.__type = 'Coat'
            self.size = int(size)

        def fabric_consumption(self):
            return (self.size/6.5 + 0.5)

        @property
        def type(self):
            return self.__type   
        
        @property
        def param(self):
            return self.size  
         

class Suit(Clothes):
    def __init__(self, height):
        self.__type = 'Suit'
        self.height = height

    def fabric_consumption(self):
            return ((self.height/100)*2 + 0.3)

    @property
    def type(self):
        return self.__type   
        
    @property
    def param(self):
        return self.height  

my_coat = Coat(44)
barney_stinson_suit = Suit(183) 
print(f'{my_coat.fabric_consumption():.2f}')
print(barney_stinson_suit.fabric_consumption())
