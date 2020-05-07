"""
Создайте собственный класс-исключение, 
который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список 
только числами. Класс-исключение должен контролировать типы данных 
элементов списка.
"""
class DigitException(Exception):
    def __str__(self):
        return 'Упс, это не число.'

buffer = []
while True:
    tmp = input('Введите число или stop: ')
    if tmp == 'stop':
        print(buffer)
        break
    else:
        try:
            if not tmp.isdigit():
                raise DigitException
            else:
                buffer.append(int(tmp))
        except DigitException as error:
            print(error)
            