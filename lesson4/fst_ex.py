# coding=utf-8
"""Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: 
(выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений 
необходимо запускать скрипт с параметрами. """
from sys import argv

_, working_time,wage_rate,reward = argv

try:
    working_time, wage_rate, reward = int(working_time),int(wage_rate),int(reward)
    print(f'Ваша зарплата: {working_time*wage_rate+reward}')
except ValueError:
    print('Неверно введеные данные. Введите целые числа.')
        