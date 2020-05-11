"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. 

Продолжить работу над первым заданием. 
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. 
Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod
from copy import deepcopy

class CountIsNotDigit(Exception):
    def __str__(self):
        return 'Количество техники не может быть нецелым числом.'

class CountOutOfLimit(Exception):
    def __str__(self):
        return 'Нельзя передать в структуру больше единиц, чем есть на складе.'


class Storehouse:
    __equipment = {
        'printer': [],
        'scanner': [],
        'copier': []
    }
    __structure_equipment = {

    }

    def get_equip(self):
        return f'{self.__equipment}'

    def get_struct_equip(self):
        return f'{self.__structure_equipment}'

    def add_equipment(self, eq_type, name, count):
        try:
            if not count.isdigit():
                raise CountIsNotDigit
            else:
                count = int(count)
        except CountIsNotDigit as error:
            print(error)
        self.__equipment[eq_type].append({name: count})

    def transfer_equipment(self, structure, eq_type, name, count):
        tmp = deepcopy(self.__equipment[eq_type])
        max_count = tmp[-1].get(name)
        try:
            if not count.isdigit():
                raise CountIsNotDigit
            else:
                count = int(count)
                if count > max_count:
                    raise CountOutOfLimit
        except CountIsNotDigit as error:
            print(error)
        except CountOutOfLimit as error:
            print(error)
        if structure not in self.__structure_equipment:
            self.__structure_equipment.update({structure: {}})
        if eq_type not in self.__structure_equipment[structure]:
            self.__structure_equipment[structure].update({eq_type: []})
        self.__structure_equipment[structure][eq_type].append({name: count})

class OfficeEquipment(ABC):

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def add_itm(self, **kwargs):
        pass

class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        self.__type = 'printer'
        self.__name = kwargs['name']
        self.__count = kwargs['count']
        self._is_color = kwargs['is_color']
        self._has_xerox = kwargs['xerox']

    @property
    def type(self):
        return f'{self.__type}'
    
    @property
    def name(self):
        return f'{self.__name}'
    
    @property
    def count(self):
        return f'{self.__count}'
    
    def add_itm(self, **kwargs):
       self.__dict__.update(kwargs)      

class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        self.__type = 'scanner'
        self.__name = kwargs['name']
        self.__count = kwargs['count']
        self._connect_type = kwargs['connect']

    @property
    def type(self):
        return f'{self.__type}'
    
    @property
    def name(self):
        return f'{self.__name}'
    
    @property
    def count(self):
        return f'{self.__count}'

    def add_itm(self, **kwargs):
       self.__dict__.update(kwargs)    

class Copier(OfficeEquipment):
    def __init__(self, **kwargs):
        self.__type = 'copier'
        self.__name = kwargs['name']
        self.__count = kwargs['count']
        self._is_color = kwargs['is_color']
    
    @property
    def type(self):
        return f'{self.__type}'
    
    @property
    def name(self):
        return f'{self.__name}'
    
    @property
    def count(self):
        return f'{self.__count}'

    def add_itm(self, **kwargs):
       self.__dict__.update(kwargs)  

my_printer = Printer(name = 'epson', count = 5, is_color = True, xerox = False)
print(my_printer.type)
my_storehouse = Storehouse()
my_storehouse.add_equipment(my_printer.type, my_printer.name, my_printer.count)
my_storehouse.transfer_equipment('бухгалтерия',my_printer.type, my_printer.name, '2' )
my_scan = Scanner(name = 'xerox', count = '2', connect = 'WI-FI')
my_storehouse.add_equipment(my_scan.type, my_scan.name, my_scan.count)
my_storehouse.transfer_equipment('бухгалтерия',my_scan.type, my_scan.name, '3' )
print(my_storehouse.get_equip())
print(my_storehouse.get_struct_equip())



        

