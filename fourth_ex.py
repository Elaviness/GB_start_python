numeral = input('Введите целое положительное число: ')

while True:
    if str(numeral).isdigit():
        numeral = int(numeral)
        break
    else:
        numeral = input('Число введено некорректно, повторите попытку: ')

max_num = 0
while numeral != 0:
    new_num = numeral % 10
    if new_num > max_num:
        max_num = new_num
    numeral = numeral // 10

print(f'Максимальная цифра во введенном числе равна {max_num}')
