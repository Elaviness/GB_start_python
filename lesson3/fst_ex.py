"""Реализовать функцию, принимающую два числа 
(позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку 
ситуации деления на ноль. """

def division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на ноль невозможно.')
        return None
    # except ValueError:
    #     print('В одном из аргументов было введено не число, попробуйте еще раз.')
    #     return None

press_key = input('Введите любой символ для начала: ')

while press_key:
    result = 0
    num_1 = input('Введите делимое: ')
    num_2 = input('Введите делитель: ')
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        print("Данные введены некорректно. Повторите еще раз.")
        continue
    result = division(num_1,num_2)
    if result:
        print(result)
    else:
        print('Операция невозможна')
    press_key = input('Для повтора введите любой символ, иначе нажмите Enter: ')
