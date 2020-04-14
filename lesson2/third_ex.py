""" Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна,
лето, осень). Напишите решения через list и через dict."""


mounth = input('Введите месяц: ')

while True:
    if mounth.isdigit() and int(mounth) <= 12:
        mounth = int(mounth)
        break
    else:
        mounth = input('Неверный формат, повторите попытку: ')

mounth_list = [('зима',(1, 2, 12)),('весна', (3,4,5)),('лето',(6,7,8)),('осень',(9,10,11))]

for itm in mounth_list:
    if mounth in itm[1]:
        result = itm[0]
print(f'Результат списка: {result}')

mounth_dict = dict(mounth_list)
if mounth in mounth_dict.values():
    result = mounth_dict.get(key)
print(f'Результат словаря: {result}')