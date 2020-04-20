num_a = input('Введите результат первого дня пробежки: ')
while True:
    if num_a.isdigit():
        num_a = int(num_a)
        break
    else:
        num_a = input('Число введено некорректно, повторите попытку: ')

num_b = input('Введите необходимый результат: ')
while True:
    if str(num_b).isdigit():
        num_b = int(num_b)
        break
    else:
        num_b = input('Число введено некорректно, повторите попытку: ')

result = num_a
i = 1

while result < num_b:
    result = 1.1*result
    i += 1

print(i)    
