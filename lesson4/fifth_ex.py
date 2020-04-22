""" Реализовать формирование списка, используя функцию range() 
и возможности генератора. В список должны войти четные числа от 100
 до 1000 (включая границы). Необходимо получить результат 
 вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

def multiplier(prev_el, el):
    return prev_el*el

new_list = [itm for itm in range(99,1001) if itm % 2 == 0]
print(reduce(multiplier, new_list))
