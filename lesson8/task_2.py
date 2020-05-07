""" Создайте собственный класс-исключение, 
обрабатывающий ситуацию деления на нуль. Проверьте его работу 
на данных, вводимых пользователем. При вводе пользователем нуля 
в качестве делителя программа должна корректно обработать эту ситуацию 
и не завершиться с ошибкой.
"""
class MyZeroDivision(Exception):
    def __str__(self):
        return 'К сожалению, человечество пока не научилось считать неопределенности.'


a,b = input('Введите делимое и делитель: '), input()
try:
    a,b = int(a), int(b)
    if b == 0:
        raise MyZeroDivision
    else:
        print(f'Результат деления: {a / b}')
except ValueError:
    print("Вы ввели не число")
except MyZeroDivision as err:
    print(err)

