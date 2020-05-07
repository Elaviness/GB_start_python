"""  Реализовать класс «Дата», функция-конструктор 
которого должна принимать дату в виде строки формата 
«день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать 
число, месяц, год и преобразовывать их тип к типу 
«Число». Второй, с декоратором @staticmethod, должен 
проводить валидацию числа, месяца и года 
(например, месяц — от 1 до 12). Проверить работу 
полученной структуры на реальных данных. """

class Date:
    def __init__(self, date):
        self.day, self.mounth, self.year = self.get_ddmmyyy(date)

    @classmethod
    def get_ddmmyyy(cls, date):
        tmp = date.split('-')
        try:
            cls.day = int(tmp[0])
            cls.mounth = int(tmp[1])
            cls.year = int(tmp[2])
            return cls.day, cls.mounth, cls.year
        except ValueError:
            print('Некорректно введенные данные.')
    
    @staticmethod
    def date_validation(date):
        tmp = date.split('-')
        try:
            day = int(tmp[0])
            mounth = int(tmp[1])
            year = int(tmp[2])
            if not 1 <= mounth <= 12: # корректность месяца
                flag = False
            else:
                if mounth in [1,3,5,7,8,10,12] and 1 <= day <= 31: # проверка на месяцы с 31 днем
                    flag = True
                elif mounth in [4,6,9,11] and 1 <= day <= 30: # проверка на месяцы с 30 днями
                    flag = True
                elif mounth == 2 and (1 <= day <= 28 or 1 <= day <= 29 and year % 4 == 0): # проверка февраля
                    flag = True
                elif 1 <= year <= 9999:
                    flag = True
                else:
                    flag = False
            return flag
        except:
            print('Одно из данных не является числом.')

        
date = '21-04-1999'
if Date.date_validation(date):
    my_date = Date(date)
    print(my_date.day)
else: 
    print("Дата введена некоректно.")
