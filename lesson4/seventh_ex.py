""" 
Реализовать генератор с помощью функции с ключевым словом
yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна 
вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикл
необходимо выводить только первые n чисел, начиная с 1! 
и до n!.
Подсказка: факториал числа n — произведение 
чисел от 1 до n. Например, факториал четырёх 
4! = 1 * 2 * 3 * 4 = 24.
"""
def fact(n=int):
    """ Подсчет факториала n-го числа"""
    tmp = 1
    for i in range(1,n+1):
        tmp *= i
        yield tmp

n = input('Ввдеите число, факториал которого хотите посчитать: ')
try:
    n = int(n)
    for _ in fact(n):
        print(_)
except ValueError:
    print('Данные введены некорректно.')