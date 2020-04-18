""" Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать 
параметры как именованные аргументы. Реализовать вывод данных 
о пользователе одной строкой. """

def user_describe(**kwargs):
    return list(kwargs.values())

name=input('Введите: имя: '),
surname=input('фамилию: '),
birth_date=input('год рождения: '),
city=input('город проживания: '),
email=input('e-mail: '),
phone_number=input('телефонный номер: ')

result = user_describe(name=name,
                    surname=surname,
                    birth_date=birth_date,
                    city=city,
                    email=email,
                    phone_number=phone_number)
print(result)
print(type(result))
