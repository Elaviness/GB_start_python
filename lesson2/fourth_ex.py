""" Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
  Если в слово длинное, выводить только первые 10 букв в слове. """

users_str = input('Введите строку из нескольких слов, рахделенных пробелами: ')
   
tmp = users_str.split(' ')

for itm in tmp:
    print(f'{itm:.10}')
    