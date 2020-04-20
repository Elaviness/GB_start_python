sec = input('Введите время в секундах: ')

while True:
    if sec.isdigit():
        sec = int(sec)
        break
    else:
        sec = input('Вы ввели не число, повторите попытку: ')

hours = sec // 3600
sec = sec - hours*3600

minutes = sec // 60
sec = sec - minutes*60

print(f'Ваше время - {hours}:{minutes}:{sec}')
