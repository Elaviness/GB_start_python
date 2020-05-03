class Cell:
    def __init__(self, units):
        self.__units = units
    
    def __add__(self, other):
        return self.__units + other.__units

    def __sub__(self, other):
        if self.__units - other.__units > 0 : 
            return self.__units - other.__units
        else:
            print('Клетка не может быть меньше, чем ничего.')    

    def __mul__(self, other):
        return self.__units * other.__units

    def __truediv__(self, other):
        return round(self.__units / other.__units)

    def make_order(self, row):
        tmp = ''
        unit = self.__units
        while True:
            if unit // row > 0:
                tmp += '*' * row +'\n'
            else:
                tmp += '*' * unit
                break
            unit -= row
        return tmp

cell = Cell(25)
cell_2 = Cell(3)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(8))

