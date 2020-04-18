"""  Программа принимает действительное положительное 
число x и целое отрицательное число y. Необходимо 
выполнить возведение числа x в степень y. Задание 
необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной 
функции возведения числа в степень. """

def my_pow_1(x,y):
    """Возведение в степень оператором ** """
    return x**y

def my_pow_2(x,y):
    """ Возведение без оператора **"""
    result = x
    for i in range(1,y):
        result *= x
        i +=1
    return result

x, y = input("Введите число и степень, в которую хотите возвести "), input()
try:
    x, y = int(x), int(y)
    print(my_pow_1(x,y))
    print(my_pow_2(x,y))
except ValueError:
    print('Данные введены некорректно.')
