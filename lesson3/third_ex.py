"""  Реализовать функцию my_func(), 
которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов. """

def max_sum(a,b,c):
    """ Возвращает сумму двух наибольших элементов"""
    tmp = [a , b ,c]
    tmp_elem = max(tmp)
    tmp.remove(tmp_elem)
    return tmp_elem + max(tmp)

a, b, c = input('Введите три числа: '), input(), input()
try:
    a, b, c = int(a), int(b), int(c)
    print(max_sum(a,b,c))
except ValueError:
    print('Данные введены некорректно.')
    