"""Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, 
определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

from itertools import count,cycle

def iter_num(n=int):
    """ Бесконечный итератор целых чисел"""
    for itm in count(n):
        print(itm)

def iter_string(string=str):
    """ Бесконечный итератор повторяющий элементы входной строки"""
    for itm in cycle(string):
        print(itm)

iter_num(5)
iter_string("ABC")
