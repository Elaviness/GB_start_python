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

class Storehouse:
    __equipment = {
        'printer': [],
        'scanner': [],
        'copier': []
    }

class OfficeEquipment(ABC):

    @property
    @abstractmethod
    def __type(self) -> str:
        pass

    @property
    @abstractmethod
    def __name(self) -> str:
        pass

    @abstractmethod
    def add_itm(self, **kwargs):
        pass

class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        __type = 'printer'
        __name = kwargs['name']
        _is_color = kwargs['is_color']
        _has_xerox = kwargs['xerox']

class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        __type = 'scanner'
        __name = kwargs['name']
        _connect_type = kwargs['connect']

class Copier(OfficeEquipment):
    def __init__(self, **kwargs):
        __type = 'copier'
        __name = kwargs['name']
        _is_color = kwargs['is_color']






        

